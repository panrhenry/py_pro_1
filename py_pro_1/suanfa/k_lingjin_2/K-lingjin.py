# K - 近邻算法 ■ - i
# 优 点 ：精度高、对异常值不敏感、无数据输入假定。
# 缺点：计算复杂度高、空间复杂度高。
# 适用数据范围：数值型和标称型

import numpy as np
import operator


def createDataset():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


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


if __name__ == '__main__':
    data = createDataset()
    print(np.tile([0, 0], (4, 1)) - data[0])
    print(classify0([9, 0], data[0], data[1], 3))
