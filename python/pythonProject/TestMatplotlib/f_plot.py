# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

# 单个
dataY = np.arange(20)
plt.plot(dataY)
plt.show()

# 指定X和Y值和线的样式
data = np.arange(20)
plt.plot(data, data**2, 'ro')
plt.show()

#同时绘制多条线
data = np.arange(20)
plt.plot(data, data**2, 'ro', data, np.exp(data), '-')
plt.show()

