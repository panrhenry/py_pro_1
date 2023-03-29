#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
"""
 @Time    : 2023/3/23 9:41
 @Author  : panrhenry
"""
import time
from playwright.sync_api import sync_playwright as playwright

pw = playwright().start()
chrom = pw.chromium.launch(headless=False)
context = chrom.new_context()  # 需要创建一个 context
page = context.new_page()  # 创建一个新的页面
page.goto("https://web.innodealing.com/auth-service/signin")
page.get_by_placeholder("DM账号/手机号").click()
page.get_by_placeholder("DM账号/手机号").click()
page.get_by_placeholder("DM账号/手机号").fill("yuyingjie")
page.get_by_placeholder("密码").click()
page.get_by_placeholder("密码").fill("123456")
page.get_by_text("我已阅读并同意相关服务条款和政策").click()
page.get_by_role("button", name="登录").click()
time.sleep(3)
page.frame_locator("iframe >> nth=0").locator(".nY5g3oU45oPl4aioSr5\\+ag\\=\\=").click()
time.sleep(1)
page.frame_locator("iframe >> nth=0").get_by_text("首页").first.click()
time.sleep(1)
page.frame_locator("iframe >> nth=0").get_by_role("button", name="历史成交").click()
time.sleep(4)
page.click('//*[@id="bondModule"]/div[1]/div[1]/div/div/div/div[1]/div/div/div[1]')
t1 = page.frame_locator("iframe >> nth=0").locator("div").filter(has_text="万科企业股份有限公司").nth(0)
time.sleep(2)
t2 = page.frame_locator("iframe >> nth=0").get_by_role("combobox").filter(has_text="万科企业股份有限公司").get_by_role("textbox")
# time.sleep(2)
page.frame_locator("iframe >> nth=0").get_by_role("combobox").filter(has_text="万科企业股份有限公司").get_by_role("textbox").fill("驻马店市产业投资集团有限公司")
time.sleep(3)
page.frame_locator("iframe >> nth=0").get_by_role("menuitem", name="驻马店市产业投资集团有限公司", exact=True).click()
time.sleep(10)
# ---------------------
context.close()
