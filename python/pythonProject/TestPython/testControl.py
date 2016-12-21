# -*-coding:utf-8 -*-
import numpy as np
max = []
min = []
for i in range(-2, 2 + 1):
    max.append(i > 0)
    min.append(i < 0)
print(max)
print(min)

# 带索引， 多列表 同时遍历
index = 0
for i, j in zip(np.array([i for i in range(1, 5)]), np.array([j for j in range(5, 10)])):
    index+= 1
    print(index, i, j)


