"""
支持向量机的数字识别：
    1. 准备数据：基于二值图像构造向量
    2. 对向量图像进行目测
    3. 训练算法： 采用两种不同的核函数，并对径向基核函数采用不同的设置来运行8厘0 算法
    4. 测试算法：计算错误率
"""
from numpy.matlib import zeros


def loadImages(dirName):
    from os import listdir
    hwLabels = []
    trainingFileList=listdir(dirName)
    fileLength = len(trainingFileList)
    trainingMat = zeros((fileLength,1024))
    for i in range(fileLength):
        fileNamestr = trainingFileList[i]
        fileStr = fileNamestr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        if classNumStr == 9:hwLabels.append(-1)
        

