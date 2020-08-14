# -*- coding: utf-8 -*-

import sys
import urllib
import urllib2
import lxml.html
import time
import cookielib

# 防止中文乱码
reload(sys)
sys.setdefaultencoding('utf8')


class dingdian_crawler(object):
    search_data = {}
    search_url_template = 'http://zhannei.baidu.com/cse/search?s={0}&entry=1&q={1}&isNeedCheckDomain=1&jump=1'
    catalog = {}
    catalog_key = {}
    lasted_article = list()

    def __init__(self, search_content=None, search_id=17233375349940438896):
        self.search_data['content'] = search_content
        self.search_data['id'] = search_id
        self.search_url = self.search_url_template.format(self.search_data['id'], \
                                                          self.search_data['content']).decode('utf-8')

    # cj = cookielib.CookieJar()
    # self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    # self.opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
    def load_search_data(self, search_content, search_id=17233375349940438896):
        self.__init__(search_content, search_id)

    def get_catalog(self):
        print
        self.search_url
        search_html = self.download_html(self.search_url)
        search_tree = lxml.html.fromstring(search_html)
        search_result = search_tree.cssselect('a[cpos="title"]')
        print
        len(search_result)

        catalog_url = search_result[0].get('href')
        print
        catalog_url
        catalog_html = self.download_html(catalog_url)
        catalog_tree = lxml.html.fromstring(catalog_html)
        catalog_elems = catalog_tree.cssselect('td.L a')

        num = len(catalog_elems)
        catalog_file = open('catalog.txt', 'w')
        i = 0
        for elem in catalog_elems:
            self.catalog[elem.text.decode('utf-8')] = elem.get('href')
            self.catalog_key[i] = elem.text.decode('utf-8')
            i += 1

        self.lasted_article = list()
        self.lasted_article.append(self.catalog_key[num - 1])
        self.lasted_article.append(self.catalog[self.catalog_key[num - 1]])

        print
        len(self.catalog)

    def get_novel_content(self, start, num=0):

        if start + int(num) > len(self.catalog_key):
            print
            'maybe out of article list range'
            print
            'please reset start or num'
            return

        if num == 0:
            url = self.get_article_url(start)
            article_html = self.download_html(url)
            soup = BeautifulSoup(article_html, 'html.parser')
            article = soup.find('dd', attrs={'id': 'contents'})
            content = '\n\n\n' + self.catalog_key[start - 1] + '\n\n\n'
            content = content + article.text.decode('utf-8')
            file_name = self.search_data['content'] + str(start) + '.txt'
            self.save_article(file_name, [content, ])
        else:
            i = 0
            contents = []
            while i < num:
                content = ''
                url = self.get_article_url(start + i)
                article_html = self.download_html(url)
                soup = BeautifulSoup(article_html, 'html.parser')
                article = soup.find('dd', attrs={'id': 'contents'})
                content = '\n\n\n' + self.catalog_key[i + start - 1] + '\n\n\n'
                content = content + article.text.decode('utf-8')
                contents.append(content)
                i = i + 1;
            file_name = self.search_data['content'] + str(start) + '-' + str(start + num - 1) + '.txt'
            self.save_article(file_name, contents)

    def get_article_url(self, index):
        try:
            print
            self.catalog[self.catalog_key[index - 1]]
            return self.catalog[self.catalog_key[index - 1]]
        except Exception:
            print
            'out of article list range'
            print
            'please reset index'

    def print_search_url(self):
        print
        self.search_url

    def save_article(self, name, articles):
        wfile = open(name, 'w')
        for article in articles:
            wfile.write(article)
        wfile.close

    def download_html(self, url, times=5):
        try:
            html = urllib2.urlopen(url).read()
            print
            'download success'
            return html
        except Exception as e:
            if times:
                print
                'download fail'
                print
                'try download again:', (6 - times)
                times = times - 1
                time.sleep(2)
                return self.download_html(url, times)
            else:
                print
                'crawl failed'
                sys.exit(1)


if __name__ == '__main__':
    crawler = dingdian_crawler('神魔乐园'.decode('utf-8'))
    crawler.get_catalog()
    print(crawler.lasted_article[0].decode('utf-8'))
