# -*-coding:utf-8 -*-
import numpy as np

# 判断两个矩阵的元素是否相等
data = np.array([1, -2, 3, -5, 6])
data1 = data > 0
data2 = data > 0
data3 = data < 0
print((data1 == data2).all())
print((data1 == data3).all())