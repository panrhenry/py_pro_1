"""
cookie
"""
import requests
# 获取cookie
response = requests.get("http://www.baidu.com")
print(response.cookies)
# 用于会话维持
session = requests.session()
session.get("http://httpbin.org/cookies/set/number/123456")
response = session.get("http://httpbin.org/cookies")
print(response.text)
# 证书验证
response = requests.get("https://www.12306.cn")
print(response.status_code)
print("----------------")

"""
proxies= {
    "http":"http://61.135.217.7:80",
    "https":"https://61.135.217.7:80"
}
response  = requests.get("https://www.baidu.com",proxies=proxies)
print(response.text)
"""

import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>',html,re.S)
print(result)
print(result.groups())
print(result.group(1))
print(result.group(2))
print("------------------------")
results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>',html,re.S)
print(results)
for result in results:
    # print(result)
    print(result[0],result[1],result[2])
print("--------------------------------------")
"""
\s*? 这种用法其实就是为了解决有的有换行，有的没有换行的问题
(<a.*?>)? 这种用法是因为html中有的有a标签，有的没有的，？表示匹配一个或0个，正好可以用于匹配
"""
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>',html,re.S)
print(results)
for result in results:
    print(result[1])
