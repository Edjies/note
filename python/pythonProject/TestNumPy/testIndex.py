# -*-coding:utf-8 -*-
import numpy as np

# 复杂的切片和索引
a = np.arange(16)**2
index = np.array([1, 3, 5, 7])
print(a[index])  # 列出每个索引位置的值

index2 = np.array([[2, 3], [6, 7]])
print(a[index2])

a.resize((8, 2))
print(a[index])
