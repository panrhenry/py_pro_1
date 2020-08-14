"""
request库的基本使用
"""
import requests, json

# response = requests.get("https://www.baidu.com")
# print(type(response))
# print(response.status_code)
# print(type(response.text))
# print(response.text)
# print(response.cookies)
# print(response.content)
# print(response.content.decode("utf-8"))

# request各种请求方式
# requests.post("http://httpbin.org/post")
# requests.put("http://httpbin.org/put")
# requests.delete("http://httpbin.org/delete")
# requests.head("http://httpbin.org/get")
# requests.options("http://httpbin.org/get")

"""
response = requests.get("http://httpbin.org/get?name=chengzhi&age=23")
print(response.text)
print("--------------------------------")
# 也可通过字典传递参数
params = {
    "name": "chengzhi",
    "age": 23,
}
response = requests.get("http://httpbin.org/get?", params=params)
print(response.url)
print(response.text)
print("-------------------------------")
"""
# 解析json
response = requests.get("http://httpbin.org/get")
print(response.json())

handers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
response = requests.get("https://www.zhihu.com", headers=handers)
print(response.text)
print("---------------------")

files= {
    "files":open("1.jpg","rb")
}
response = requests.post("http://httpbin.org/post",files=files)
print(response.text)
