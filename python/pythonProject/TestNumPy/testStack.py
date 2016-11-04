# -*-coding:utf-8 -*-
import numpy as np

# 组合
a = np.floor(10 * np.random.random((2, 3)))
print(a)
b = np.floor(10 * np.random.random((2, 3)))
print(b)
c = np.vstack((a, b))   # vertical stack
print(c)
d = np.hstack((a, b))  # horizontal stack
print(d)
#  e = np.vstack((c, d))   #  error
#  print(e)

# 分割
for array in np.hsplit(d, 3):  # 横向分割， 必须为等距分割
    print(array)

for array in np.vsplit(c, 2):  # 纵向分割, 必须为等距分割
    print(array)

for array in np.vsplit(c, (1, 2, 3)):  # 纵向分割， 设定分割线 [0-1), [1-2), [2-3), [3-)
    print(array)


