import numpy as np
import operator
from os import listdir

file_trainging_dir = "C:\\Users\panrui\Desktop\learning file\machinelearninginaction\Ch02\\trainingDigits"
file_test_dir = "C:\\Users\panrui\Desktop\learning file\machinelearninginaction\Ch02\\testDigits"


# 训练模型
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = np.tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()  # 排序 根据值大小从小到大，取其索引值
    classCount = {}
    for i in range(k):
        voteLabel = labels[sortedDistIndicies[i]]
        classCount[voteLabel] = classCount.get(voteLabel, 0) + 1
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# 将图像处理为一个向量 ,循环读出文件的前32行
def img2vector(filename):
    returnVect = np.zeros((1, 1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    hwlabels = []
    traningfileList = listdir(file_trainging_dir)
    m = len(traningfileList)
    traningMat = np.zeros((m, 1024))
    for i in range(m):
        filenameStr = traningfileList[i]
        classNumberStr = int(filenameStr.split('.')[0].split('_')[0])
        hwlabels.append(classNumberStr)
        traningMat[i, :] = img2vector(file_trainging_dir + "\\" + filenameStr)
    testFileList = listdir(file_test_dir)
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        filenameStr = testFileList[i]
        classNumberStr = int(filenameStr.split('.')[0].split('_')[0])
        vectorUnderTest = img2vector(file_test_dir + "\\" + filenameStr)
        classfierResult = classify0(vectorUnderTest, traningMat, hwlabels, 5)
        print("the classifier came back with: %d,the real answer is: %d" % (classfierResult, classNumberStr))
        if (classfierResult != classNumberStr):
            errorCount += 1
    print("\nthe total number of errors is : %d" % errorCount)
    print("\nthe total error rate is ： %f" % (errorCount / float(mTest)))


if __name__ == '__main__':
    # filename = "C:\\Users\panrui\Desktop\learning file\machinelearninginaction\Ch02\\trainingDigits\\0_1.txt"
    # array1 = img2vector(filename)
    # print(array1[0,0:31])
    handwritingClassTest()
