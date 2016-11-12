# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# 同一幅图上显示多张图片， 第一个参数代表多少行， 第二个参数代表多少列， 第三个参数代表位置
data = np.arange(20)
plt.subplot(2, 2, 1)
plt.plot(data, data)

plt.subplot(2, 2, 2)
plt.plot(data, data**2)

plt.subplot(2, 2, 3)
plt.plot(data, data**3)

plt.show()