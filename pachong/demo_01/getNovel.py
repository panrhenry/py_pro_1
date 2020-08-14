# https://www.zhaishuyuan.com/
import re
import urllib.request

def getNovelContent():
    html = urllib.request.urlopen("https://www.zhaishuyuan.com/").read()
    html = html.decode('gbk')
    print(html)
    pass

if __name__ == '__main__':
    getNovelContent()