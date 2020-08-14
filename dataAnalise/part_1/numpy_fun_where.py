import numpy as np
from numpy.matlib import randn

arr = randn(4, 4)
print(arr)

# 将>0的数赋为2，否则 = -2
print(np.where(arr > 0, 2, -2))

# 将>0的数赋为2，否则 为原值
print(np.where(arr > 0, 2, arr))

if __name__ == '__main__':
    pass
