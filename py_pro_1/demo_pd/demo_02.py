from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# np.nan : nan 表示NAN
df = DataFrame([[1.3, np.nan], [2.5, 6.8], [24.5, np.nan], [3.6, 2.1]], index=['a', 'b', 'c', 'd'],
               columns=['one', 'two'])
# print(df)
# sum默认按列进行求和，戴上参数axis=1 则按行求和
print(df.sum())
print(df.sum(axis=0))
