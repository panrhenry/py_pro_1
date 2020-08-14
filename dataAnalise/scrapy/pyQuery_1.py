"""
pyquery 库的使用
"""
from pyquery import PyQuery as pq
# 初始化 初始化的时候一般有三种传入方式：传入字符串，传入url,传入文件
# 字符串初始化
html = '''
<div id="container">
    <ul class="list">
         <li class="item-0">first item</li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
         <li class="item-1 active"><a href="link4.html">fourth item</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a></li>
     </ul>
 </div>
 '''
doc = pq(html)
# print(doc)
# print(doc('li'))
# print(doc('.item-0'))
# url初始化
# doc = pq(url="http://www.baidu.com",encoding='utf-8')
# print(doc('head'))
print(doc('#container .list li'))

items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)