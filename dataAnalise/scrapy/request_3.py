"""
正则表达式的使用
\w      匹配字母数字及下划线
\W      匹配f非字母数字下划线
\s      匹配任意空白字符，等价于[\t\n\r\f]
\S      匹配任意非空字符
\d      匹配任意数字
\D      匹配任意非数字
\A      匹配字符串开始
\Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
\z      匹配字符串结束
\G      匹配最后匹配完成的位置
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开头
$       匹配字符串的末尾
.       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
[^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符
*       匹配0个或多个的表达式
+       匹配1个或者多个的表达式
?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
{n}     精确匹配n前面的表示
{m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
a|b     匹配a或者b
()      匹配括号内的表达式，也表示一个组
"""
# re.compile 将正则表达式编译成正则表达式对象，方便复用
import requests, re
import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
content = requests.get("https://book.douban.com/").text
# f = open("test.txt",'w',encoding="utf-8")
# f.write(content)
# f.close()
pattern = re.compile(
    '<li.*?cover.*?href="(.*?)" title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?publisher">(.*?)</span>.*?".*?</li>',
    re.S)
results = re.findall(pattern, content)
print(results[0])
for result in results:
    url, name, author, date, publisher = result
    author = re.sub('\s', '', author)
    date = re.sub('\s', '', date)
    publisher = re.sub('\s', '', publisher)
    print(url, name, author, date, publisher)
