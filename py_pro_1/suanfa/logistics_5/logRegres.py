"""
训练算法：使用梯度上升找到最佳系数
伪代码:
    1.回归系数全部初始化为1
    重复R次：
        计算整个数据集的梯度
        使用alpha * gradient 更新回归系数的向量
        返回回归系数
2.append,extend的区别：append是将wordList当做一个对象加入，extend是将wordList看作一个序列添加
3.np.mat()： 用于创建矩阵
"""
import random

import numpy as np
import matplotlib.pyplot as plt


# 加载数据集，
def loadDataSet():
    dataMat = []
    labelMat = []
    fr = open("D:\panrui\我的桌面\learning file\machinelearninginaction\Ch05\\testSet.txt")
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat, labelMat


def sigmoid(inX):
    return 1.0 / (1 + np.exp(-inX))


# 梯度上升算法
def gradascent(dataMat, labelMat):
    # 将加载进来的数据集转化为numpy矩阵
    dataMatrix = np.mat(dataMat)
    # np.mat(labelMat)得到的是1*100行向量，transpose()获得它的转置，得到列向量便于计算
    labelMat = np.mat(labelMat).transpose()
    m, n = np.shape(dataMatrix)
    alpha = 0.001
    maxCpcles = 500
    # 构建n行1列的数组
    weights = np.ones((n, 1))
    for k in range(maxCpcles):
        # 矩阵相乘，运用signoid公式计算
        h = sigmoid(dataMatrix * weights)
        error = (labelMat - h)
        #
        weights = weights + alpha * dataMatrix.transpose() * error
    return weights


# 随机梯度上升算法
def stocGradAscent0(dataMat, labelMat):
    dataMat = np.array(dataMat)
    m, n = np.shape(dataMat)
    alpha = 0.01
    weights = np.ones(n)
    for i in range(m):
        h = sigmoid(sum(dataMat[i] * weights))
        error = labelMat[i] - h
        weights = weights + alpha * error * dataMat[i]
    weights = np.mat(weights).reshape((3, 1))
    return weights


# 改进的随机梯度上升算法
def stocGradAscent1(dataMat, labelMat, numIter=150):
    dataMat = np.array(dataMat)
    m, n = np.shape(dataMat)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4 / (1.0 + j + i) + 0.01
            randIndex = int(random.uniform(0, len(dataIndex)))
            h = sigmoid(sum(dataMat[randIndex] * weights))
            error = labelMat[randIndex] - h
            weights = weights + alpha * error * dataMat[randIndex]
            del (dataIndex[randIndex])
    return weights


# 画出数据集和logistic回归的最佳拟合直线
def plotbestFit(wei):
    weights = np.mat(wei).reshape((3, 1))
    weights = weights.getA()
    dataMat, labelMat = loadDataSet()
    dataArr = np.array(dataMat)
    n = np.shape(dataArr)[0]
    xcord1 = []
    ycord1 = []
    xcord2 = []
    ycord2 = []
    for i in range(n):
        if (labelMat[i]) == 1:
            xcord1.append(dataArr[i, 1])
            ycord1.append(dataArr[i, 2])
        else:
            xcord2.append(dataArr[i, 1])
            ycord2.append(dataArr[i, 2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s')
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)
    # 最佳拟合直线 z=w0*x0+w1*x1+w2*x2+... 另z=0,x0=1
    y = (-weights[0] - weights[1] * x) / weights[2]
    ax.plot(x, y)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()


# ----------------------------
# logistic回归分类函数
def classifyVector(inX, weights):
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5:
        return 1.0
    else:
        return 0.0


def colicTest():
    frTrain = open('D:\panrui\我的桌面\learning file\machinelearninginaction\Ch05\horseColicTraining.txt')
    frTest = open('D:\panrui\我的桌面\learning file\machinelearninginaction\Ch05\horseColicTest.txt')
    trainingSet = []
    trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
    trainWeights = stocGradAscent1(np.array(trainingSet), trainingLabels, 500)
    errorCount = 0
    numTestVec = 0.0
    for line in frTest.readlines():
        numTestVec += 1.0
        currLine = line.strip().split('\t')
        lineArr = []
        for i in range(21):
            lineArr.append(currLine[i])
        if int(classifyVector(np.array(lineArr), trainWeights)) != int(currLine[21]):
            errorCount += 1
    errorRate = (float(errorCount) / numTestVec)
    print('the error rate of this test is ：%f' % errorRate)
    return errorRate


def nultiTest():
    numTests = 10
    errorSum = 0.0
    for k in range(numTests):
        errorSum += colicTest()
    print('after %d iterations the average error rate is: %f' % (numTests, errorSum / float(numTests)))


# -----------------------------------


if __name__ == '__main__':
    # dataMat, labelMat = loadDataSet()
    # # weights = gradascent(dataMat, labelMat)
    # weights = stocGradAscent1(dataMat, labelMat)
    # plotbestFit(weights)
    nultiTest()
