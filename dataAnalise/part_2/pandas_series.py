#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/08/17 13:32
# @Author  : panrhenry
# @Email   : panrhenry@163.com
import numpy
from pandas import Series, DataFrame
import pandas as pd

# Series 类似于一维数组的对象，由一组数据及一组与之相关的标签组成
# ------------------------------------------------------------------------------------
# obj = Series([4, 7, 5, 2])
obj = Series([4, 7, 5, 2], index=['d', 'a', 'x', 'b'])
print(obj.values)
print(obj.index)
print(obj['d'])
print('-------------------')
# 数组运算
print(obj[obj > 3], obj * 2, numpy.exp(obj))


def func_dropna():
    """dropna:  返回一个非空数据和索引值的Series"""
    data = Series([1, None, 3.5, None, 7])
    print(data.dropna())
    data1 = DataFrame([[1, 6.5, 3.],
                       [1, None, None],
                       [None, None, None],
                       [None, 6.5, 3.]])
    cleaned = data1.dropna()
    data1.dropna(how='all')  # g过滤全为空的行

    data1[4] = None
    data1.dropna(axis=1, how='all')  # 过滤全为空的列 关键语句：axis=1







if __name__ == '__main__':
    pass
