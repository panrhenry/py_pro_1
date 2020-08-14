import numpy as np

# 数学统计方法

# 包含函数： mean() ,
#           cumsum() , cumprod()  不聚合，产生一个由中间结果组成的数组


# mean()函数功能：求取均值
# mean() 函数定义：
# numpy.mean(a, axis, dtype, out，keepdims )
# 经常操作的参数为axis，以m * n矩阵举例：
#
# axis 不设置值，对 m*n 个数求均值，返回一个实数
# axis = 0：压缩行，对各列求均值，返回 1* n 矩阵
# axis =1 ：压缩列，对各行求均值，返回 m *1 矩阵

arr = np.random.randn(5, 4)

print(arr.mean())
print(arr.mean(axis=1))

# cumsum() 累计和  相加
# cumprod() 累计积 相乘
# axis = 0 按列  ; axis=1 按行
arr1 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
arr1.cumsum(0)     #按列相加
arr1.cumprod(1)    #按行相乘


if __name__ == '__main__':
    pass
