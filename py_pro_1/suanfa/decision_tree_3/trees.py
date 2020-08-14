"""
使用决策树进行分类
"""
import py_pro_1.suanfa.decision_tree.dec_tree_01 as dt
import py_pro_1.suanfa.decision_tree.treePlotter as tp


# 使用决策树的分类函数
def classify(inputTree, featLabels, testVec):
    firstStr = list(inputTree.keys())[0]
    secondDict = inputTree[firstStr]
    # 将标签字符串转化为索引,匹配第一个标签变量的元素
    featIndex = featLabels.index(firstStr)
    for key in secondDict.keys():
        if testVec[featIndex] == key:
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                classLabel = secondDict[key]
    return classLabel


"""
storeTree，grabTree：
使用pickle模块存储决策树,可以将分类器存储在硬盘上
"""


def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'wb+')
    pickle.dump(inputTree, fw)
    fw.close()


def grabTree(filename):
    import pickle
    fr = open(filename, 'rb')
    return pickle.load(fr)


if __name__ == '__main__':
    # myDat, labels = dt.createDataSet()
    # print(myDat,labels)
    # myTree = tp.retriveTree(0)
    # print(myTree)
    # storeTree(myTree, 'E:\kaifa_profile\data\python\classifierStorage.txt')
    # grabTree('E:\kaifa_profile\data\python\classifierStorage.txt')
    # print(classify(myTree, labels, [1, 0]))
    # 隐形眼镜数据集加载

    fr = open("E:\panrui\我的桌面\learning file\machinelearninginaction\Ch03\lenses.txt")
    # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
    lenses = [inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels = ['age', 'tearRate', 'astigmatic', 'prescript']
    lensesTree = dt.createTree(lenses, lensesLabels)
    # print(lensesTree)
    tp.createPlot(lensesTree)
