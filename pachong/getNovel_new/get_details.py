import time

import os
from playwright.sync_api import sync_playwright, Playwright
import pandas as pd
import re


def data_details(page):
    """获取当前页明细数据"""
    # details = page.frame_locator("iframe >> nth=0").get_by_role("row").all_inner_texts()
    details_1 = page.frame_locator("iframe >> nth=0").get_by_role("row").get_by_role("cell").all_inner_texts()
    columns = details_1[0:15]
    columns.pop()
    df = pd.DataFrame(columns=columns)
    i = 15
    while i <= len(details_1) - 1:
        detail = details_1[i:i + 15]
        detail.pop()
        df.loc[len(df)] = detail
        i = i + 15
    time.sleep(2)
    df.to_csv("detail_zq.csv", encoding='utf_8_sig', mode='a')
    getdetails_fy(page)


def getdetails_fy(page):
    """加载下一页明细数据"""
    # 下一页标签
    try:
        page.frame_locator("iframe >> nth=0").get_by_role("button", name="图标: right").click()
        time.sleep(2)
    except Exception as e:
        print("已到最后一页，进行下一个搜索")
        return "已完成當前公司数据"

    data_details(page)


def search_company(page, origin_name, companyname):
    """按公司搜索加载明细数据"""
    page.frame_locator("iframe >> nth=0").get_by_title(origin_name).first.click()
    time.sleep(2)
    page.frame_locator("iframe >> nth=0").get_by_role("combobox") \
        .filter(has_text=origin_name).get_by_role("textbox").fill(companyname)
    time.sleep(2)
    page.frame_locator("iframe >> nth=0").get_by_role("menuitem", name=companyname, exact=True).click()
    time.sleep(3)
    data_details(page)
    # 完成明细遍历，更改origin_name
    origin_name = companyname
    return origin_name


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web.innodealing.com/auth-service/signin")
    page.get_by_placeholder("DM账号/手机号").click()
    page.get_by_placeholder("DM账号/手机号").fill("yuyingjie")
    page.get_by_placeholder("DM账号/手机号").press("Enter")
    time.sleep(1)
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").fill("123456")
    time.sleep(1)
    page.get_by_text("我已阅读并同意相关服务条款和政策").click()
    page.get_by_role("button", name="登录").click()
    time.sleep(6)
    page.frame_locator("iframe >> nth=0").locator(".nY5g3oU45oPl4aioSr5\\+ag\\=\\=").click()
    time.sleep(2)
    page.frame_locator("iframe >> nth=0").get_by_text("首页").first.click()
    time.sleep(2)
    page.frame_locator("iframe >> nth=0").get_by_role("button", name="历史成交").click()
    time.sleep(5)
    # 初始公司名称
    # 循环读取公司txt
    origin_name = "万科企业股份有限公司"
    companyname = "万科企业股份有限公司"
    # 删除csv数据
    if os.path.isfile("detail_zq.csv"):
        os.remove('detail_zq.csv')
    f = open("company.txt", 'r', encoding='utf-8')
    lines = f.readlines()
    for line in lines:
        companyname = line.replace('\n', '')
        origin_name = search_company(page, origin_name, companyname)

    time.sleep(2)
    # ---------------------
    context.close()
    browser.close()


if __name__ == '__main__':
    with sync_playwright() as playwright:
        run(playwright)
