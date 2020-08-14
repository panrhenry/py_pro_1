import urllib.request


def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html


def content(html):
    str = '<article class="excerpt excerpt-one">'
    content = html.partition(str)[2]
    str1 = '<p class="note">'
    content = content.partition(str1)[2]
    return content


def title(content, beg=0):
    try:
        title_list = []
        while beg >= 0:
            num1 = content.index('】', beg)
            num2 = content.index('</p>', num1)
            title_list.append(content[num1: num2])
            beg = num2
    except ValueError:
        return title_list


def get_title():
    pass


# 获取图片的url
def image(content, beg=0):
    # 思路是利用str.index()和序列的切片
    try:
        img_list = []
        while True:
            src1 = content.index('http', beg)
            src2 = content.index('/></p>', src1)
            img_list.append(content[src1:src2])
            beg = src2

    except ValueError:
        return img_list


if __name__ == '__main__':
    content = content(str(getHtml("https://bh.sb/post/category/main/"), encoding="utf-8"))
    # title = title(content)
    # for i, e in enumerate(title):
    #     print('第%d个，title:%s' % (i, e))
    image = image(content)
    for i, e in enumerate(image):
        print('第%d个，title:%s' % (i, e))
