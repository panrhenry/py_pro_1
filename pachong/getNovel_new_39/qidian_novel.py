#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
"""
 @Time    : 2023/3/27 15:31
 @Author  : panrhenry
 限免小说爬取
"""
import re
import time
import os
from playwright.sync_api import Playwright, sync_playwright


def login(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.qidian.com/")
    page.get_by_role("link", name="登录").click()
    time.sleep(3)
    page.frame_locator("iframe[name=\"frameLG\"]").get_by_role("paragraph") \
        .filter(has_text="请先点击同意协议登录即代表同意 《用户服务协议》 和 《隐私政策》") \
        .locator("label").click()
    page.frame_locator("iframe[name=\"frameLG\"]").get_by_text("QQ登录").click()
    with page.expect_popup() as page1_info:
        page.frame_locator("iframe[name=\"frameLG\"]").get_by_text("前去登录QQ").click()
    page1 = page1_info.value
    page1.frame_locator("iframe[name=\"ptlogin_iframe\"]").locator('//*[@id="qlogin_list"]/a').click()
    time.sleep(5)
    # 重新加载页面
    page.reload()
    time.sleep(5)
    # 运行
    run(page)
    context.close()
    browser.close()


def run(page):
    page.get_by_role("link", name="免费", exact=True).click()
    time.sleep(3)
    page_1 = page.query_selector('#limit-list').query_selector('.book-img-text').query_selector_all('.book-mid-info')
    # 获取限免小说名称目录
    novel_names = []
    for content in page_1:
        novel_names.append(content.query_selector('h2').inner_text())

    # 循环获取小说内容
    for novel_name in novel_names:
        # 删除相关文本
        novel_file = novel_name + ".txt"
        if os.path.isfile(novel_file):
            os.remove(novel_file)
        fo = open(novel_file, 'wb+')

        with page.expect_popup() as page1_info:
            page.get_by_role("link", name=novel_name, exact=True).click()
            time.sleep(3)
        page1 = page1_info.value

        page1.locator('.j_catalog_block').click()
        time.sleep(3)
        # page1.get_by_role("link", name="目录").click()
        # 获取小说具体章节
        book_chap_names = page1.query_selector('.volume-wrap').query_selector_all('.book_name')
        # currnet_chap = ''
        # try:
        #     # 获取当前存档章节，章节标题,从上次章节开始爬取
        #     currnet_chap = page1.query_selector('.read-progress') \
        #         .query_selector('.progress-name').inner_text().strip()
        # except Exception as e:
        #     print("账号i未登录，无上次阅读章节记录")
        for book_chap_name in book_chap_names:
            with page1.expect_popup() as page2_info:
                bcn = book_chap_name.inner_text()
                page1.get_by_role("link", name=bcn).last.click()
                time.sleep(8)
            page2 = page2_info.value
            # page2.get_by_role("link", name="").click()
            # 章节标题
            chapter_name = bcn
            # chapter_name = page2.query_selector('.j_chapterName').query_selector('.content-wrap').inner_html()

            fo.write(('\r' + chapter_name + '\r\n').encode('UTF-8'))

            # 内容正文
            contents = page2.query_selector('.read-content.j_readContent').query_selector_all('.content-wrap')
            time.sleep(3)

            # ---------------------
            for content in contents:
                content_text = re.sub('\s+', '\r\n\t', content.inner_html())
                fo.write(("" + "\r\n").encode("UTF-8"))
                fo.write(content_text.encode('UTF-8'))
            page2.close()

        page1.close()

        # 测试，单本
        break


with sync_playwright() as playwright:
    login(playwright)
