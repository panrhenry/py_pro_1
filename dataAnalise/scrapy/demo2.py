"""
高级用法各种handler
代理,ProxyHandler
通过rulllib.request.ProxyHandler()可以设置代理,网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，
它会禁止你的访问,所以这个时候需要通过设置代理来爬取数据

cookie的存储及获取
"""
import urllib.request
import http.cookiejar

proxy_handler = urllib.request.ProxyHandler(
    {
        'http': 'http://61.135.217.7:80',
        'https': 'https://61.135.217.7:80'
    }
)
opener = urllib.request.build_opener(proxy_handler)
responce = opener.open('http://httpbin.org/get')
print(responce.read())
print("--------------------------------")
"""
cookie,HTTPCookiProcessor
cookie中保存中我们常见的登录信息，有时候爬取网站需要携带cookie信息访问,这里用到了http.cookijar，
用于获取cookie以及存储cookie
"""
cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
responce = opener.open("http://www.baidu.com")
for item in cookie:
    print(item.name + "=" + item.value)
print("-----------------------------")

"""
cookie可以写入到文件中保存，有两种方式http.cookiejar.MozillaCookieJar和http.cookiejar.LWPCookieJar()
"""
# http.cookiejar.MozillaCookieJar()方式
filename = "cookie.txt"
cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)

# http.cookiejar.LWPCookieJar()方式
filename = "cookie.txt"
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
cookie.save(ignore_discard=True, ignore_expires=True)

# 通过获取文件中的cookie获取的话可以通过load方式，当然用哪种方式写入的，就用哪种方式读取
cookie = http.cookiejar.LWPCookieJar()
# cookie = http.cookiejar.MozillaCookieJar()
cookie.load("cookie.txt", ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
# print(response.read().decode("utf-8"))


