"""
朴素贝叶斯算法
"""
from numpy import *


def loadDataSet():
    postingList = [
        ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
        ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
        ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
        ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
        ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
        ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']
    ]
    classVec = [0, 1, 0, 1, 0, 1]  # 1代表污辱性文字，0为正常言论
    return postingList, classVec


# 取出数据集中所有的元素，并去重重复元素
def createVocabList(dataSet):
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


# 即判断输入数据集inputSet的集是否存在于vocablist,并且统计存在的元素出现的次数，返回统计出来的词频
def setOfWords2Vec(vocablist, inputSet):
    # returnVec [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    returnVec = [0] * len(vocablist)
    for word in inputSet:
        if word in vocablist:
            returnVec[vocablist.index(word)] = 1
        else:
            print("the world: %s is not my Vocabulary！" % word)
    return returnVec


# 朴素贝叶斯分类器训练函数
def trainNB0(trainMatrix, trainCategory):
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 初始化概率
    p0Num = ones(numWords)
    p1Num = ones(numWords)
    p0Demon = 2
    p1Demon = 2
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            # 向量相加，生成一个新的数组当中的值即为对应元素出现的次数，p1Demon为所有元素的总数
            p1Num += trainMatrix[i]
            p1Demon += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Demon += sum(trainMatrix[i])
    #  ln(a*b)=lna+lnb
    p1Vect = log(p1Num / p1Demon)
    p0Vect = log(p0Num / p0Demon)
    return p0Vect, p1Vect, pAbusive


# 分类函数，计算概率
def classifyNB(vec2Classify, p0Vect, p1Vect, pAbusive):
    p1 = sum(vec2Classify * p1Vect) + log(pAbusive)
    p0 = sum(vec2Classify * p0Vect) + log(1.0 - pAbusive)
    if p1 > p0:
        return 1
    else:
        return 0

# 文档词袋模型，词袋中每个单词可出现多次，与上面的词集模型不同
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


# 便利函数，封装所有操作，节省时间
def testingNB():
    listOPosts, listClasses = loadDataSet()
    # 返回无重复的数据集
    myVocaList = createVocabList(listOPosts)
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocaList, postinDoc))
    p0Vect, p1Vect, pAbusive = trainNB0(trainMat, listClasses)
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocaList, testEntry))
    print(testEntry, 'classified as:', classifyNB(thisDoc, p0Vect, p1Vect, pAbusive))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocaList, testEntry))
    print(testEntry, 'classified as:', classifyNB(thisDoc, p0Vect, p1Vect, pAbusive))


if __name__ == '__main__':
    """
    listOPosts, listClasses = loadDataSet()
    # myVocaList 获取到的是数据集无重复元素的所有集
    myVocaList = createVocabList(listOPosts)
    # print(myVocaList)
    # print(setOfWords2Vec(myVocaList, listOPosts[3]))
    # trainMat 用于存储统计出的词频，即数据集每个文档在无重复数据集的个数统计
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocaList, postinDoc))
    p0Vect, p1Vect, pAbusive = trainNB0(trainMat, listClasses)
    # print(p0Vect)
    # print(p1Vect)
    # print(pAbusive)
    """
    testingNB()
