"""
url解析
"""
from urllib.parse import urlparse, urlunparse, urljoin, urlencode

result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
# 指定协议拆分
result1 = urlparse("www.baidu.com/index.html;user?id=5#comment", scheme="https")
print(result)
print(result1)
print("-------------------------------x")
# urlunpars功能和urlparse的功能相反，它是用于拼接
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=123', 'commit']
print(urlunparse(data))
print("----------------------------------")
# urljoin 拼接的时候后面的优先级高于前面的url
print(urljoin('http://www.baidu.com', 'FAQ.html'))
print(urljoin('http://www.baidu.com', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html', 'https://pythonsite.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc', 'https://pythonsite.com/index.php'))
print(urljoin('http://www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com', '?category=2#comment'))
print(urljoin('www.baidu.com#comment', '?category=2'))
print("--------------------------------")
# urlencode 将字典转化为url参数
params = {
    "name": "chengzhi",
    "age": "23"
}
base_url = "http://www.baidu.com?"
url = base_url + urlencode(params)
print(url)
