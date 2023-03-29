#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
 @Time    : 2023/3/21 16:04
 @Author  : panrhenry
 @Email   : panrhenry@163.com
"""
import time
from selenium import webdriver
import json

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# 需访问页面
# goal_url = 'https://web.innodealing.com/dashboard/'

goal_url = 'https://web.innodealing.com/quote-web/#/bond/historical-market'


def browser_initial():
    """"
    浏览器初始化,登陆页面
    """
    browser = webdriver.Chrome()
    browser.get("https://web.innodealing.com/auth-service/signin")
    return browser


def getdetails_fy():
    pass


def log_damai(browser):
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
    time.sleep(5)


    # 全部债券列表
    all_1 = browser.find_element(By.XPATH, '//*[@id="all"]')

    t1 = browser.find_element(By.XPATH, '//*[@id="bondModule"]/div[1]/div[1]/div/div/div/div[1]')

    t1.click()


    browser.frame


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

    #需完成点击分页按钮，递归调取，直至最后一页
    # 还没写
    getdetails_fy()

    browser.quit()

    print(np_xy)


if __name__ == "__main__":
    # 生成cookie
    from getNovel.get_cookie import get
    # get()
    browser = browser_initial()
    log_damai(browser)
