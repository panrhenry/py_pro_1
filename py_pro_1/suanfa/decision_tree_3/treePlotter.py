# 使用patplotlib的注解功能绘制树形图
import matplotlib.pyplot as plt


# 创建一棵树,用于测试代码
def retriveTree(i):
    listOfTrees = [{
        'no surfacing': {
            0: 'no',
            1: {
                'flippers': {
                    0: 'no',
                    1: 'yes'
                }
            },
            3: 'maybe'
        }
    }, {
        'no surfacing': {
            0: 'no',
            1: {
                'flippers': {
                    0: {
                        'head': {
                            0: 'no',
                            1: 'yes'
                        }
                    },
                    1: 'no'
                }
            }
        }
    }]
    return listOfTrees[i]


# 定义文本框和箭头格式
decisionNode = dict(boxstyle='sawtooth', fc="0.8")
leafNode = dict(boxstyle='round4', fc="0.8")
arrow_args = dict(arrowstyle='<-')


# 绘制带箭头的注解
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction',
                            xytext=centerPt, textcoords='axes fraction',
                            va='center', ha='center', bbox=nodeType, arrowprops=arrow_args)


# 定义两函数，获取叶子节点的数目和树的层数
def getNumLeafs(myTree):
    numLeafs = 0
    # 获取字典key的集合，取第一个值
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    # print(list(secondDict.keys()))
    for key in secondDict.keys():
        # 判断key所取的值是否任然为字典类型，若是则递归调用方法(进入下一层)
        if type(secondDict[key]).__name__ == 'dict':
            numLeafs += getNumLeafs(secondDict[key])
        else:
            numLeafs += 1
    return numLeafs


# 获取树的层数
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == 'dict':
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            thisDepth = 1
        if thisDepth > maxDepth:
            maxDepth = thisDepth
    return maxDepth


# 在父子节点之间填充文本信息
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString)


# 计算宽与高,使用这两个变量来计算的树的摆放位置，可以将树绘制在水平位置和垂直位置的中心位置
# 变量plotTree.xOff，plotTree.yOff追踪已经绘制的节点位置，以及放置下一个节点的恰当位置。
# 使用plotMidtxt()计算父节点与子节点的中间位置，以便添加简单的文本标签信息
# 按照叶子节点的个数将x轴划分为若干部分
def plotTree(myTree, parentPt, nodeTxt):
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    cntrPt = (plotTree.xOff + float(1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    # 标记子节点属性值,在父子节点之间填充文本信息
    plotMidText(cntrPt, parentPt, nodeTxt)
    # 绘制带箭头的注解
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    # 减少y偏移,根据树的高度计算每次减少y值的量，即y=y-1/h
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        if type(secondDict[key]).__name__ == "dict":
            plotTree(secondDict[key], cntrPt, str(key))
        else:
            # 改变x轴的偏移量，x=x+1/w
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD


# 绘制树的主函数，调用了plotTree(),
def createPlot(inTree):
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    plotTree.xOff = -0.5 / plotTree.totalW
    plotTree.yOff = 1.0
    # print(plotTree.totalW,plotTree.totalD,plotTree.xOff,plotTree.yOff)
    # 4.0 2.0 -0.125 1.0
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()


if __name__ == '__main__':
    myTree = retriveTree(0)
    createPlot(myTree)
    # print(getNumLeafs(myTree), getTreeDepth(myTree))
