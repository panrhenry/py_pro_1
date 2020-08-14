"""
selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）
和测试的并行处理（Selenium Grid）。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，
因此可以用于任何支持JavaScript的浏览器上。
selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。
"""
from selenium import webdriver

# 声明并调用浏览器
browser = webdriver.Chrome()
browser.get("http://www.taobao.com")

# print(browser.page_source)
# browser.close()

# ---------------------
# 单个元素查找
input_first = browser.find_element_by_id("q")
input_second = browser.find_element_by_css_selector("#q")
input_third = browser.find_element_by_xpath('//*[@id="q"]')
print(input_first)
print(input_second)
print(input_third)

"""
常用查找元素方法：
find_element_by_name
find_element_by_id
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
"""
# 比较通用的方式：by模块
from selenium.webdriver.common.by import By

browser.get("http://www.taobao.com")
input_4 = browser.find_element(By.ID, "q")
print(input_4)

# 多个元素查找（find_elements ）:
lis = browser.find_elements_by_css_selector('.service-bd li')
print(lis)

browser.close()
# -------------------------------------
# 元素交互操作
import time

browser = webdriver.Chrome()
browser.get("http://www.taobao.com")
input_str = browser.find_element_by_id('q')


# -------------------------------------
