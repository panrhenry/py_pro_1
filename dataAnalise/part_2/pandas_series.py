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
print(obj[obj > 3],obj * 2, numpy.exp(obj))

if __name__ == '__main__':
    pass
