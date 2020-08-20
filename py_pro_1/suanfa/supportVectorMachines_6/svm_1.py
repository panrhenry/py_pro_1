"""
基于最大间隔分割数据
    优点：泛化错误率低，计算开销低，结果易于解释
    缺点：对参数调节和核函数的选择敏感，原始分类器不加修改仅适用于二类问题
    适用数据类型：数值型和标称型数据
"""
import random


def loadDataSet(fileName):
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split("\t")
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat


def selectJrand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))
    return j


def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if aj < L:
        aj = L
    return aj


if __name__ == '__main__':
    txt = "D:\panrui\我的桌面\learning file\machinelearninginaction\Ch06\\testSet.txt"
    dataArr, labelArr = loadDataSet(txt)
    print(labelArr)
