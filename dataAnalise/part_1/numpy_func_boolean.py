#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Time    : 2020/08/14 16:13
# @Author  : panrhenry
# @Email   : panrhenry@163.com

#  布尔型数组
import numpy as np
from numpy.matlib import randn

arr = randn(100)
print( (arr > 0).sum() )

# any (一个或多个)，all （所有）
bools = np.array([False,True,False,False])
bools.any()  # out : true
bools.all()  # out : false


if __name__ == '__main__':
    pass
