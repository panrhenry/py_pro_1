"""
smo算法的第一个版本：
伪代码：
    当迭代次数小于最大迭代次数时(外循环)
        对数据集的每个数据向量(内循环)
            如果该向量可以被优化：
                随机选择另外一个响亮
                同时优化这两个向量
                如果两个向量都不能被优化，退出内循环
        若果所有的都没有被优化，增加迭代数目，继续下一次循环
"""
from numpy import mat, shape, zeros, multiply
import suanfa.supportVectorMachines_6.svm_1 as sv1


def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    """简化版SMO算法"""
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    b = 0
    m, n = shape(dataMatrix)
    alphas = mat(zeros((m, 1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas, labelMat).T * \
                        (dataMatrix * dataMatrix[i, :].T)) + b
            Ei = fXi - float(labelMat[i])
            if ((labelMat[i] * Ei < -toler) and (alphas[i] < C) or
                    ((labelMat[i] * Ei > toler) and (alphas[i] > 0))):
                j = sv1.selectJrand(i, m)
                fXj = float(multiply(alphas, labelMat).T * \
                            (dataMatrix * dataMatrix[j, :].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[i] + alphas[j] - C)
                    H = min(C, alphas[i] + alphas[j])
                if L == H:
                    print("L==H")
                    continue
                eta = 2.0 * dataMatrix[i, :] * dataMatrix[j, :].T - \
                      dataMatrix[i, :] * dataMatrix[i, :].T - \
                      dataMatrix[j, :] * dataMatrix[j, :].T
                if eta>=0:
                    print("eta>=0")
                    continue
                
