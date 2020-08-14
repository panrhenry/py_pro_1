from math import log
import operator


# 创建数据集
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']
               ]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 计算信息熵，熵：信息的期望值，即信息源的不确定度，信息的量化度量问题
def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prod = float(labelCounts[key]) / numEntries
        shannonEnt -= prod * log(prod, 2)
    return shannonEnt


# 按照给定特征划分数据集，数据集，特征，返回值
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])  # 集合内元素逐个追加
            retDataSet.append(reducedFeatVec)  # 作为整体追加
    return retDataSet


# 选择最好的数据集划分方式
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestFeature):
            bestFeature = infoGain
            bestFeature = i
    return bestFeature


# 递归构建决策树，
"""
1.得到原始数据集，然后基于最好的属性划分数据集，由于特征值存在多个的情况，因此存在大于两个分支的数据集划分
2.第一次划分之后，数据将被划分到树分支的下一个节点，在这个节点上，可以再次划分数据。
3.递归结束的条件：程序遍历完所有划分数据集的属性，或者每个分支下的所有实例都具有相同的分类。
    如果所有的实例具有相同的分类，则得到一个叶子节点或者终止块。任何到达叶子结点的数据必然属于叶子节点的分类
"""


def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    # 类别完全相同则停止继续划分
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # 遍历完所有特征时返回次数出现最多的
    if len(dataSet[0]) == 1:
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel: {}}
    # 得到列表包含的所有属性值
    del (labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
    return myTree


"""
mayplotlib注解工具：annotations,可在数据图形上添加文本，通常用于解释数据的内容

"""


def majorityCnt(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount


if __name__ == '__main__':
    dataSet, lables = createDataSet()
    # shannonEnt = calcShannonEnt(dataSet)
    # print(shannonEnt)
    # print(splitDataSet(dataSet,0,1))
    # result = chooseBestFeatureToSplit(dataSet)
    # print(result)
    mytree = createTree(dataSet, lables)
    print(mytree.keys(), mytree)
