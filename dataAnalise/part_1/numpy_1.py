# np.meshgrid :  将两个一维数组，产生一个二维数组
import numpy as np
import matplotlib.pyplot as plt

points = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points, points)

# xs ** 2 即求平方 ，sqrt : 求开方
z = np.sqrt(xs ** 2 + ys ** 2)

plt.imshow(z, cmap=plt.cm.gray)
plt.colorbar()
plt.title("image plot of ")

plt.show()

if __name__ == '__main__':
    pass
