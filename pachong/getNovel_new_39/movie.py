#!/usr/bin/python3.6
#-*- coding: utf-8 -*-
"""
 @Time    : 2023/3/22 10:27
 @Author  : panrhenry
"""

import time
from selenium import webdriver
import json
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://web.innodealing.com/auth-service/signin")
