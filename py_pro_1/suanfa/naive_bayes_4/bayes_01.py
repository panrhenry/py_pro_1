"""
使用朴素贝叶斯过滤垃圾邮件
"""
from numpy import *

from py_pro_1.suanfa.naive_bayes.bayes import createVocabList, setOfWords2Vec, trainNB0, classifyNB, bagOfWords2VecMN
import random
import feedparser

file_path_spam = 'E:\panrui\我的桌面\learning file\machinelearninginaction\Ch04\email\spam\\'
file_path_ham = 'E:\panrui\我的桌面\learning file\machinelearninginaction\Ch04\email\ham\\'

"""
解析文本：
    1.lower():统一成小写 ，upper():大写
    2.采用正则表达式过滤，以除去字母数字意外的字符作为分隔符
"""


# 文本解析
def textParse(bigString):
    import re
    regEx = re.compile('\\W*')
    listOfTokens = regEx.split(bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = []
    classList = []
    fullText = []
    # 导入并解析文本
    for i in range(1, 26):
        wordList = textParse(open(file_path_spam + '%d.txt' % i).read())
        # append,extend的区别：append是将wordList当做一个对象加入，extend是将wordList看作一个序列添加
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        wordList = textParse(open(file_path_ham + '%d.txt' % i).read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    # 返回一个无重复的数据集
    vocabList = createVocabList(docList)
    # python3 ,range返回的是range对象，而不是数组对象，只需加入list()
    # 构建训练集，测试集
    trainingSet = list(range(50))
    testSet = []
    # 随机构建训练集，在trainingSet下标范围内随机生成10个index,并添加到testSet
    for i in range(10):
        # random.uniform() 在[a,b)随机生成一个实数
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(trainingSet[randIndex])
        # 目的是删除已选到的下标值，是元素不重复
        del trainingSet[randIndex]
    trainMat = []
    trainClasses = []
    for docIndex in trainingSet:
        # 统计词频
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
    print("the error rate is: ", float(errorCount) / len(testSet))


"""
从个人广告中获取区域倾向
收集数据：RSS收集内容
"""


# 计算词出现的频率
def calcMostFreq(vocabList, fullText):
    import operator
    freDict = {}
    for token in vocabList:
        freDict[token] = fullText.count(token)
    sortedFreq = sorted(freDict.items(), key=operator.itemgetter(1), reverse=True)
    return sortedFreq[:30]


def localWords(feed1, feed0):
    docList = []
    classList = []
    fuulText = []
    # print([i for i in list(feed1.keys()) if feed1[i] != []])
    # print(list(feed1.keys()), feed0['entries'])
    minLen = min(len(feed1['entries']), len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])
        docList.append(wordList)
        fuulText.extend(wordList)
        classList.append(1)
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fuulText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    top30Words = calcMostFreq(vocabList, fuulText)
    # 去掉出现次数最高的词
    # for pairW in top30Words:
    #     if pairW[0] in vocabList:
    #         vocabList.remove(pairW[0])
    trainingSet = list(range(2 * minLen))
    testSet = []
    for i in range(10):
        randIndex = int(random.uniform(0, len(trainingSet)))
        testSet.append(randIndex)
        del trainingSet[randIndex]
    trainingMat = []
    trainingClasses = []
    for docIndex in trainingSet:
        trainingMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainingClasses.append(classList[docIndex])
    p0Vect, p1Vect, pAbusive = trainNB0(array(trainingMat), array(trainingClasses))
    errorCount = 0
    for docIndex in testSet:
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(array(wordVector), p0Vect, p1Vect, pAbusive) != classList[docIndex]:
            errorCount += 1
    print('the error rate is: ', float(errorCount) / len(testSet))
    return vocabList, p0Vect, p1Vect


# 最具表特征的词汇显示函数


if __name__ == '__main__':
    # spamTest()
    ny = feedparser.parse('http://www.nasa.gov/rss/dyn/image_of_the_day.rss')
    sf = feedparser.parse('http://sports.yahoo.com/nba/teams/hou/rss.xml')
    vocabList, p0Vect, p1Vect = localWords(ny, sf)
