# numpy 是高性能科学计算和数据分析的基础包
# ndarray : 一个具有矢量算术运算 的多维数组
# 线性代数，随机数生成，及傅里叶变化功能
# 对于整组数据进行快速运算的标准数学函数（无需编写循环）
# 用于集成 由C,C++,Fortran等语言编写的代码的工具

# 创建ndarray
import numpy as np

data1 = [3, 6.5, 8, 1, 0]
array1 = np.array(data1)
print(array1)

# ----------------------------
data_2 = [
    [1, 2, 3, 4],
    [7, 9, 3, 0]
]
array_2 = np.array(data_2)
print(array_2)
print(array_2.ndim, array_2.dtype)

print(np.zeros((2, 6)))
print(np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')]))

print(np.empty((2, 3, 2)))

data_3 = np.eye(3)

print(data_3)
