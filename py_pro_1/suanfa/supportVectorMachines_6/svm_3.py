# 完整版platt SMO 的支持函数
from numpy import shape, zeros, mat, multiply, nonzero

from suanfa.supportVectorMachines_6.svm_1 import selectJrand


class optStruct:
    def __init__(self, dataMatIn, classLabels, C, toler):
        self.X = dataMatIn
        self.lableMat = classLabels
        self.C = C
        self.toler = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m, 1)))
        self.b = 0
        # 误差缓存
        self.eCache = mat(zeros((self.m, 2)))

    def calcEk(self, oS, k):
        fXk = float(multiply(oS.alphas, oS.lableMat)).T * (oS.X * oS.X[k:].T) + oS.b
        Ek = fXk - float(oS.lableMat[k])
        return Ek

    def selectJ(self, i, oS, Ei):
        maxK = -1
        maxDeltaE = 0
        Ej = 0
        oS.eCache[i] = [1, Ei]
        validEacheList = nonzero(oS.eCache[:, 0].A)[0]
        if len(validEacheList) > 1:
            for k in validEacheList:
                if k == i:
                    continue
                Ek = self.calcEk(oS, k)
                deltaE = abs(Ei - Ek)
                if (deltaE > maxDeltaE):
                    maxK = k
                    maxDeltaE = deltaE
                    Ej = Ek
            return maxK, Ej
        else:
            j = selectJrand(i, oS.m)
            Ej = self.calcEk(oS, j)
        return j, Ej

    def updateEk(self, oS, k):
        Ek = self.calcEk(oS, k)
        oS.eCache[k] = [1, Ek]
