#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
 @Time    : 2023/3/21 16:04
 @Author  : panrhenry
"""
import time
from selenium import webdriver
import json
from selenium.webdriver.common.by import By

# 需访问页面
# goal_url = 'https://web.innodealing.com/dashboard/'

goal_url = 'https://web.innodealing.com/quote-web/#/bond/historical-market'

savepath = 'result.txt'


# 保存数据
def writeData(datalist, savepath):
    with open(savepath, mode="a", encoding="utf-8") as f:
        for data in datalist:
            f.write(data)  # 写数据
            f.write("\n")  # 换行
        f.close()


def browser_initial():
    """"
    浏览器初始化,登陆页面
    """
    browser = webdriver.Chrome()
    browser.get("https://web.innodealing.com/auth-service/signin")
    return browser


def getdetails_fy(browser):
    """加载下一页明细数据"""
    # 下一页标签
    next_pages = browser.find_element(By.XPATH,
                                      '//*[@id="bondModule"]/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div[2]/button[3]')

    if next_pages.get_attribute('disabled'):
        # 终止，返回结果
        return "已到最后一页，终止"
    # 点击下一页获取数据
    next_pages.click()
    time.sleep(3)
    # 暂时使用数组存，，，可写入txt文件
    data_details(browser)
    getdetails_fy(browser)


def data_details(browser):
    """获取当前页明细数据"""
    # 全部债券列表
    # all_1 = browser.find_element(By.XPATH, '//*[@id="all"]')

    # 债券明细
    details = browser.find_element(By.XPATH,
                                   '//*[@id="bondModule"]/div[1]/div[2]/div/div[3]/div/div[1]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div[2]/table/tbody') \
        .find_elements(By.TAG_NAME, 'tr')

    np_xy = []
    for i in details:
        ll = []
        j = i.find_elements(By.TAG_NAME, 'td')
        for item in j:
            text = item.text
            ll.append(text)
        np_xy.append(ll)
    writeData(np_xy, savepath)



    # return np_xy


def log_result(browser):
    """
    从本地读取cookies并刷新页面,成为已登录状态
    """
    # 首先清除由于浏览器打开已有的cookies
    browser.delete_all_cookies()

    with open('login_cookies.txt', 'r', encoding='utf8') as f:
        listCookies = json.load(f)

    # 往browser里添加cookies
    for cookie in listCookies:
        # 并不是所有cookie都含有expiry 所以要用dict的get方法来获取
        if isinstance(cookie.get('expiry'), float):
            cookie['expiry'] = int(cookie['expiry'])
        browser.add_cookie(cookie)

    browser.get(goal_url)
    # 需等待完全加载数据出来
    time.sleep(6)

    np_xy = []

    np_xy = data_details(browser)

    # 需完成点击分页，调取，直至最后一页
    # 还没写
    np_xy = getdetails_fy(browser)

    browser.quit()

    print(np_xy)


if __name__ == "__main__":
    # 生成cookie
    from getNovel_new_39.get_cookie import get

    # get()
    browser = browser_initial()
    log_result(browser)
