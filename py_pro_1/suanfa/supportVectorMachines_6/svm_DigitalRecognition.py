"""
支持向量机的数字识别：
    1. 准备数据：基于二值图像构造向量
    2. 对向量图像进行目测
    3. 训练算法： 采用两种不同的核函数，并对径向基核函数采用不同的设置来运行8厘0 算法
    4. 测试算法：计算错误率
"""
from numpy.matlib import zeros, mat, nonzero, shape, multiply, sign
import numpy as np
import smopy


# 将图像处理为一个向量 ,循环读出文件的前32行
def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def kernelTrans(X, A, kTup):
    m, n = np.shape(X)
    K = np.mat(np.zeros((m, 1)))
    if kTup[0] == 'lin':
        K = X * A.T
    elif kTup[0] == 'rbf':
        for j in range(m):
            deltaRow = X[j, :] - A
            K[j] = deltaRow * deltaRow.T
        K = np.exp(K / (-1 * kTup[1] ** 2))
    else:
        raise NameError('Houston we hava a problem the kernel is not recognized')
    return K


def loadImages(dirName):
    from os import listdir
    hwLabels = []
    trainingFileList = listdir(dirName)
    fileLength = len(trainingFileList)
    trainingMat = zeros((fileLength, 1024))
    for i in range(fileLength):
        fileNamestr = trainingFileList[i]
        fileStr = fileNamestr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        if classNumStr == 9:
            hwLabels.append(-1)
        else:
            hwLabels.append(1)
        trainingMat[i:] = img2vector('%s/%s' % (dirName, fileNamestr))
    return trainingMat, hwLabels


def testDigits(kTrup=('rbf', 10)):
    dataArr, labelArr = loadImages('trainingDigits')
    b, alphas = smopy(dataArr, labelArr, 200, 0.0001, 10000, kTrup)
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    svInd = nonzero(alphas.A > 0)[0]
    sVs = datMat[svInd]
    labelSV = labelMat[svInd]
    print("there are %d Support Vectors " % shape(sVs)[0])
    m, n = shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], kTrup)
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print("the training error is: %f" % (float(errorCount) / m))
    dataArr, labelArr = loadImages('testDigits')
    errorCount = 0
    datMat = mat(dataArr)
    labelMat = mat(labelArr).transpose()
    m, n = shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs, datMat[i, :], kTrup)
        predict = kernelEval.T * multiply(labelSV, alphas[svInd]) + b
        if sign(predict) != sign(labelArr[i]):
            errorCount += 1
    print("the training error is: %f" % (float(errorCount) / m))

if __name__ == '__main__':
    testDigits(('rbf',20))
