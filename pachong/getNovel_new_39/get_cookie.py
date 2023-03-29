#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
 @Time    : 2023/3/21 13:34
 @Author  : panrhenry
"""
import json
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def cookie_exist(driver):
    cookies = driver.get_cookies()
    jsonCookies = json.dumps(cookies)  # 转换成字符串保存
    with open('login_cookies.txt', 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')


def get():
    f = open('conf.yaml')
    data = f.read()
    yaml_reader = yaml.load(data, Loader=yaml.Loader)

    loginname = yaml_reader['loginname']
    password = yaml_reader['password']

    driver = webdriver.Chrome()
    driver.set_window_size(1124, 850)  # 防止得到的WebElement的状态is_displayed为False，即不可见
    driver.get("https://web.innodealing.com/auth-service/signin")
    time.sleep(2)
    elem = driver.find_element(By.ID, "inputUsername")
    elem.clear()
    elem.send_keys(loginname)
    time.sleep(2)

    paword = driver.find_element(By.ID, "inputPassword")
    paword.clear()
    paword.send_keys(password)
    time.sleep(2)

    gx = driver.find_element(By.ID, "approve-privacy")
    gx.click()

    elem.send_keys(Keys.RETURN)
    time.sleep(3)

    # cookies存
    cookie_exist(driver)

    driver.quit()


if __name__ == '__main__':
    get()
