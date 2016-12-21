# -*-coding:utf-8 -*-
import numpy as np

# 判断两个矩阵的元素是否相等
data = np.array([1, -2, 3, -5, 6])
data1 = data > 0
data2 = data > 0
data3 = data < 0
print((data1 == data2).all())
print((data1 == data3).all())

#切割
data = np.array([1, 2, 3, 4])
data2 = np.array([1, 2, 4, 5])
print(data2[1:3])
print(np.min(data2[1:3]))

#比较
data = np.array([-1, -2, -3])
data1 = data < 0
data2 = np.array([True] * 3)
print(((data < 0) == np.array([True] * 3)).all())
print(np.sum(data))


