from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# Series类似于一维数组的对象，由一组数据以及一组与之相关的数据标签(即索引)组成，

obj = Series([4, 1, 7, 3])
print(obj)

print(obj.values, obj.index)  # 可获取值与索引

obj2 = Series([4, 1, 2, 9], index=['a', 'b', 'c', 'd'])

print(obj2)
print(obj2.index)
print(obj2[['a', 'c', 'd']])
print(obj2 * 2)
print(np.exp(obj2))  # e 的 x 次方

# 如果数据被存放在一个python字典中，可直接通过字典创建series
data_1 = {'a1': 2121, 'a2': 312321, 'a3': 2121}
print(Series(data_1))
# 也可重新指定索引名, 有序排列（指定顺序）
states = ['a2', 'a3', 'a1']
obj3 = Series(data_1, index=states)
obj3.name = 'propertity'
obj3.index.name = 'state'
print(obj3)

# dataFrame ,二维结构，行列都有索引（表格）
data_2 = {
    's1': ['cz', 'pr', 'zhi', 'pan'],
    's2': [4.3, 3.2, 4.9, 321.90],
    's3': [1, 6, 4, 8]
}
frame_1 = DataFrame(data_2, columns=['s2', 's3', 's1'])
print(frame_1)
print(frame_1['s1'], frame_1.s2)
