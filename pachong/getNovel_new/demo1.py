"""加载下一页明细数据"""
    # 下一页标签
import os


def demo1():
    try:
        print(11)
    except Exception as e:
        print("已到最后一页，终止")
        return "已完成當前公司数据"
    print(11222)

def demo2():
    # 以二进制形式打开指定文件
    f = open("company.txt", 'r',encoding='utf-8')
    byt = f.readlines()
    for line in byt:
        print(line.replace('\n',''))

if __name__ == '__main__':
    demo2()
    if (os.path.isfile("detail_zq.csv")):
        os.remove('detail_zq.csv')
