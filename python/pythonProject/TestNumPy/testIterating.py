# -*-coding:utf-8 -*-
import numpy as np

a = np.arange(20)
a.shape = (4, 5)
# 遍历每一行
for row in a:
    print(row)


# 遍历元素
for element in a.flat:
    print(element)

