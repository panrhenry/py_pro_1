# coding:utf-8
import requests
import json

from lxml import html
from selenium import webdriver

query = '贾静雯'
''' 下载图片 '''


def download(src, id):
    dir = 'E:\panrui\我的桌面\learning file\data\py\pic3\\' + str(id) + '.jpg'
    try:
        pic = requests.get(src, timeout=10)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except requests.exceptions.ConnectionError:
        print('图片无法下载')


src_xpath = "//div[@class='item-root']/a[@class='cover-link']/img[@class='cover']/@src"
title_path = "//div[@class='item-root']/div[@class='detail']/div[@class='title']/a[@class='title-text']"
# chromedriver.exe 的路径
driver_path = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=driver_path, options=options)
driver.get("https://movie.douban.com/")
srcs = html.xpath(src_xpath)
titles = html.xpath(title_path)
for src, title in zip(srcs, titles):
    download(src, title.text)
