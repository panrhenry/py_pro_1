"""
自聚汇聚法：bootstrap aggregating ,元数据集选择S次后得到一个S个新数据集，元数据集等于新数据集
AdaBoost为每个分类器都分配了一个权重值alpha，这些alpha值是基于每个弱分类器的错误
率进行计算的。
"""
from operator import le

from numpy import matrix, shape, ones, mat, zeros, inf, log, multiply, exp, sign

"""
np.matrix([[1, 2], [3, 4]])
    matrix([[1, 2],
            [3, 4]])


"""


def loadSimpleData():
    datMat = matrix([[1.0, 2.1], [2.0, 1.1], [1.3, 1.0], [1.0, 1.], [2., 1.]])
    classLabels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return datMat, classLabels


"""

第一个函数将用于测试是否有某个值小于或者大于我们正在测试的阈值。
第二个函数则更加复杂一些，它会在一个加权数据集中循环，并找到具有最低错误率的单层决策树。

将最小错误率minError设为+00
对数据集中的每一个特征（第一层循环）：
    对 每 个 步 长 （第二层循环）：
        对每 个不 等 号 （第三层循环）：
            建立一棵单层决策树并利用加权数据集对它进行测试
            如果错误率低于m in Err0r ，则将当前单层决策树设为最佳单层决策树
返回最佳单雇决策树

代码位置：程序清单7-1
"""


def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = ones((shape(dataMatrix)[0], 1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0
    return retArray


"""
D: 权重向量
"""


def buildStump(dataArr, classLabels, D):
    dataMatrix = mat(dataArr)
    # print("dataMatrix:  %s" % dataMatrix)
    labelMat = mat(classLabels).T
    # print("labelMat:  %s" % labelMat)
    # 获取矩阵行列数值 五行两列
    m, n = shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClassEst = mat(zeros((m, 1)))
    print(bestClassEst)
    # 初始化成无穷大，之后用于寻找可能的最小错误率
    minError = inf
    """
    三层嵌套的for循环是程序最主要的部分。第一层for循环在数据集的所有特征上遍历。考
    虑到数值型的特征，我们就可以通过计算最小值和最大值来了解应该需要多大的步长。然 后 ，第
    二层for循环再在这些值上遍历。甚至将阈值设置为整个取值范围之外也是可以的。因此，在取
     值范围之外还应该有两个额外的步骤。最后一个for循环则是在大于和小于之间切换不等式
    """
    for i in range(n):
        rangeMin = dataMatrix[:, i].min()
        rangeMax = dataMatrix[:, i].max()
        stepSize = (rangeMax - rangeMin) / numSteps
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = stumpClassify(dataMatrix, i, threshVal, inequal)
                errArr = mat(ones((m, 1)))
                errArr[predictedVals == labelMat] = 0
                weightdError = D.T * errArr
                # %d 整形 ， %.2f  浮点型（2 表示两位小数 ）
                print("split: dim %d, thresh %.2f, thresh ineqal: %s, the weightd error is %.3f" \
                      % (i, threshVal, inequal, weightdError))
                if weightdError < minError:
                    minError = weightdError
                    bestClassEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump, minError, bestClassEst


"""程序清单7-2
输入参数：数据集，类别标签，迭代次数
"""


def adaBoostTrainDs(dataArr, classLabels, numIt=40):
    """基于单层决策树的AdaBoost训练过程"""
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m, 1)) / m)
    aggClassEst = mat(zeros((m, 1)))
    for i in range(numIt):
        # 返回值为：具有最小错误率的单层决策树，最小的错误率，估计的类别向量
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        print("D: %s" % D.T)
        alpha = float(0.5 * log((1.0 - error) / max((error, 1e-16))))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)
        print('classEst: %s' % classEst.T)
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))
        D = D / D.sum()
        aggClassEst += alpha * classEst
        print('aggClassEst: %s ' % aggClassEst.T)
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        print('total error: %s ,\n' % errorRate)
        if errorRate == 0.0:
            break
    return weakClassArr


def adaClassify(datToClass, classifierArr):
    """AdaBoost分类函数"""
    datMatrix = mat(datToClass)
    m = shape(datMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))
    for i in range(len(classifierArr)):
        classEst = stumpClassify(datMatrix, classifierArr[i]['dim'],
                                 classifierArr[i]['thresh'],
                                 classifierArr[i]['ineq'])



if __name__ == '__main__':
    D = mat(ones((5, 1)) / 5)
    datMat, classLabels = loadSimpleData()
    # print(datMat)
    # buildStump(datMat, classLabels, D)
    adaBoostTrainDs(datMat, classLabels, 9)
