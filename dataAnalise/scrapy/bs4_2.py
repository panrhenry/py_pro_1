from bs4 import BeautifulSoup

html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')
# 获取p标签的子集内容
print(soup.p.contents)
print("----------------------------")
print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i,child)

print(soup.descendants)
"""
父节点和祖先节点 通过soup.a.parent就可以获取父节点的信息
通过list(enumerate(soup.a.parents))可以获取祖先节点，这个方法返回的结果是一个列表，
会分别将a标签的父节点的信息存放到列表中，以及父节点的父节点也放到列表中，并且最后还会讲整个文档放到列表中，
所有列表的最后一个元素以及倒数第二个元素都是存的整个文档的信息
兄弟节点:
soup.a.next_siblings 获取后面的兄弟节点
soup.a.previous_siblings 获取前面的兄弟节点
soup.a.next_sibling 获取下一个兄弟标签
souo.a.previous_sinbling 获取上一个兄弟标签
"""


