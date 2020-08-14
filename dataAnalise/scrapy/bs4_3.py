# 标准选择器
# css选择器
from bs4 import BeautifulSoup
html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
# findall
soup = BeautifulSoup(html,'lxml')
list_ul = soup.find_all('ul')
print(type(soup.find_all('ul')[0]))
for ul in list_ul:
    print(ul.find_all('li'))
print("---------------------------")
# attr：  attrs可以传入字典的方式来查找标签，但是这里有个特殊的就是class,因为class在python中是特殊的字段，
# 所以如果想要查找class相关的可以更改attrs={'class_':'element'}或者soup.find_all('',{"class":"element})，
# 特殊的标签属性可以不写attrs，例如id
a = soup.find_all(attrs={'id':'list-1'})
b = soup.find_all(attrs={"class":"list list-small"})
print(a,b)

# text
print(soup.find_all(text="Bar"))
print("------------------------------")
"""
find(name,attrs,recursive,text,**kwargs)
find返回的匹配结果的第一个元素
其他一些类似的用法：
find_parents()返回所有祖先节点，find_parent()返回直接父节点。
find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点
"""


"""
通过select()直接传入CSS选择器就可以完成选择
熟悉前端的人对CSS可能更加了解，其实用法也是一样的
.表示class #表示id
标签1，标签2 找到所有的标签1和标签2
标签1 标签2 找到标签1内部的所有的标签2
[attr] 可以通过这种方法找到具有某个属性的所有标签
[atrr=value] 例子[target=_blank]表示查找所有target=_blank的标签
"""
print(soup.select('.panel .panel-heading'))
print(soup.select('ul li'))
print(soup.select('#list-1 .element'))
# 获取内容
for li in soup.select('li'):
    print(li.get_text())
# 获取属性
for ul in soup.select('ul'):
    print(ul['id'])
    # print(ul.attrs['id'])