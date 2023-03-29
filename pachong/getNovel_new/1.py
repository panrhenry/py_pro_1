import requests
import threading
from bs4 import BeautifulSoup
import re
import os
import time
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED

# 构建网页头部字典
req_hander = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '_abcde_qweasd=0; BAIDU_SSP_lcr=https://www.baidu.com/link?url=MGzrt5SpqPvHFzPSOi4wuwjH3GNPY-ERovDzdN2QygS&wd=&eqid=9948ddff00193bf4000000035d43cd1f; _abcde_qweasd=0; Hm_lvt_169609146ffe5972484b0957bd1b46d6=1564724518; bdshare_firstime=1564724517896; Hm_lpvt_169609146ffe5972484b0957bd1b46d6=1564724554',
    'Host': 'www.xbiquge.la',
    'If-Modified-Since': 'Thu, 01 Aug 2019 05:17:52 GMT',
    'If-None-Match': 'W/"5d427600-139ea"',
    'Referer': 'http://www.xbiquge.la/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
"""
分析页面：
    1. class="bookname" <h1>   章节标题
            class="bottem1"  获取上一章节，下一章节，目录
    2.id="content"   章节内容
    
    encode 编码， decode 解码
"""


# demo，获取特定章节
def getChapter():
    req_url = req_url_bas + "10/10489/"  # 特定小说地址
    chapter = "9688143.html"  # 特定章节
    #     请求当前章节页面
    r = requests.get(req_url + chapter, params=req_hander)
    # 固定编码请求
    r.encoding = 'utf-8'
    #    soup 转换
    soup = BeautifulSoup(r.text, "html.parser")
    #     获取章节名称
    chapter_name = soup.select('#wrapper .content_read .box_con .bookname h1')[0].text
    # 获取章节文本
    chapter_text = soup.select('#wrapper .content_read .box_con #content')[0]
    # 删除无用项
    for ss in chapter_text.select("script"):
        ss.decompose()
    # 按指定格式替换章节内容
    chapter_text = re.sub('\s+', '\r\n\t', chapter_text.text).strip('\r\n')
    # 写入文件
    fileName = ""
    writeToFile(chapter_name, chapter_text, fileName)
    # print('章节名： ' + chapter_name)
    # print('章节内容： \n' + chapter_text)


def writeToFile(chapter_name, chapter_text, fileName, Catalog):
    """单一章节写入文件"""
    if "" == fileName:
        file = 'D:\learning_file\pachong\\1.txt'
    else:
        file = Catalog + "\\" + fileName + ".txt"
    fo = open(file, "ab+")
    fo.write(('\r' + chapter_name + '\r\n').encode('UTF-8'))
    fo.write(chapter_text.encode('UTF-8'))
    fo.close()
    # print('已写入章节：' + chapter_name)


def dealWithFile():
    """txt文件观看优化"""
    pass


"""
小说下载函数
id：小说编号
txt字典项介绍
title：小说题目
first_page：第一章页面
txt_section：章节地址
section_name：章节名称
section_text：章节正文
section_ct：章节页数
"""


def getTxt(book_url, Catalog):
    txt = {}
    txt['title'] = ''
    try:
        # print("请输入要下载的小说编号")
        # txt['id'] = input()
        # req_url = req_url_bas + txt['id'] + '/'
        req_url = book_url
        res = requests.get(req_url, params=req_hander)
        res.encoding = 'UTF-8'
        soups = BeautifulSoup(res.text, "html.parser")
        #     获取小说题目
        txt['title'] = soups.select('#wrapper .box_con #maininfo #info h1')[0].text
        txt['mess'] = soups.select('#wrapper .box_con #maininfo #info p')
        txt['author'] = txt['mess'][0].text
        txt['updateTime'] = txt['mess'][2].text
        txt['lately'] = txt['mess'][3].text
        #     小说简介
        txt['intro'] = soups.select('#wrapper .box_con #maininfo #intro p')[1].text.strip()
        print("小说名：《" + txt['title'] + "》  开始下载。")
        # print("正在寻找第一章页面。。。")
        # 获取小说所有章节信息
        page = soups.select('#wrapper .box_con #list dl dd a')
        chapter_len = len(page)
        first_page = page[0]['href'].split('/')[3]
        chapter = first_page
        fo = open(Catalog + '\\{0}.txt.download'.format(txt['title']), "ab+")
        fo.write((txt['title'] + "\r\n").encode('UTF-8'))
        fo.write((txt['author'] + "\r\n").encode('UTF-8'))
        fo.write((txt['updateTime'] + "\r\n").encode('UTF-8'))
        fo.write((txt['lately'] + "\r\n").encode('UTF-8'))
        fo.write(("*******简介*******\r\n").encode('UTF-8'))
        fo.write(("\t" + txt['intro'] + "\r\n").encode('UTF-8'))
        fo.write(("******************\r\n").encode('UTF-8'))
        a = 1
        b = 1
        while (1):
            try:
                # 请求路径
                r = requests.get(req_url + chapter, params=req_hander)
                r.encoding = 'utf-8'
                #    soup 转换
                soup = BeautifulSoup(r.text, "html.parser")
                #     获取章节名称
                chapter_name = soup.select('#wrapper .content_read .box_con .bookname h1')[0].text
                # 获取章节文本
                chapter_text = soup.select('#wrapper .content_read .box_con #content')[0]
                # 删除无用项
                for ss in chapter_text.select("script"):
                    ss.decompose()
                # 按指定格式替换章节内容
                chapter_text = re.sub('\s+', '\r\n\t', chapter_text.text).strip('\r\n')
                # 写入文件
                # writeToFile(chapter_name, chapter_text, txt['title'])
                fo.write(('\r' + chapter_name + '\r\n').encode('UTF-8'))
                fo.write(chapter_text.encode('UTF-8'))
                # print(txt['title'] + ' 章节：' + chapter_name + '     已下载')
                a = a + 1
                if (a > chapter_len):
                    print("小说名：《" + txt['title'] + "》 下载完成")
                    break
                # 获取下一章地址
                chapter = soup.select('#wrapper .content_read .box_con .bookname .bottem1 a')[3]['href'].split('/')[3]
            except:
                print("小说名：《" + txt['title'] + "》 章节:" + chapter_name + "下载失败,正在重新尝试。")
                b = b + 1
                # 重试20次后跳出循环
                if b > 20:
                    break
        fo.close()
        os.rename(Catalog + '\\{0}.txt.download'.format(txt['title']),
                  Catalog + '\\{0}.txt'.format(txt['title']))
    except:
        pass


def getAllNovelFromUrl_1(url_1, Catalog):
    """获取该分类的所有小说"""
    start_time = time.time()  # 开始时间
    req_url = url_1
    res = requests.get(req_url, params=req_hander)
    res.encoding = 'UTF-8'
    soups = BeautifulSoup(res.text, "html.parser")
    all_books = soups.select('#wrapper #main #content #newscontent .r ul li .s2 a')
    # print(all_books)
    # print(len(all_books))
    # 设定并发量
    executor = ThreadPoolExecutor(max_workers=15)
    future_tasks = [executor.submit(getTxt, all_books[i]['href'], Catalog) for i in range(len(all_books))]
    wait(future_tasks, return_when=ALL_COMPLETED)
    # 统计所用时间
    end_time = time.time()
    print('Total cost time:%s' % (end_time - start_time))
    # for i in range(len(all_books)):
    #     book_url = all_books[i]['href']
    #     getTxt(book_url, Catalog)


def getCatagory(req_url_bas):
    """生成地址"""
    req_url = req_url_bas
    res = requests.get(req_url, params=req_hander)
    res.encoding = 'UTF-8'
    soups = BeautifulSoup(res.text, "html.parser")
    classification = soups.select('#wrapper .nav ul li a')
    if len(classification) == 0:
        print("获取内容失败，正在重新获取")
        getCatagory(req_url_bas)
    for i in range(3, 8):
        category = classification[i].text
        address = classification[i]["href"]
        # print(category+"-"+address)
        # 新建文件夹(若不存在)
        if not os.path.exists(file + category):
            os.mkdir(file + category)
        Catalog = file + category
        #     得到一个大分类的url
        url_1 = req_url_bas + address
        # 获取该分类的所有小说
        getAllNovelFromUrl_1(url_1, Catalog)


def readConfigFile():
    """从外部读取配置文件"""
    pass


if __name__ == '__main__':
    # coding:utf-8
    # getChapter()
    # 逐步读取
    req_url_bas = "http://www.xbiquge.la"  # 主地址
    file = 'D:\learning_file\pachong\\'  # 存放主路径
    # 读取配置文件 支持可配置
    # readConfigFile()
    getCatagory(req_url_bas)
    # getTxt(10489)
