# -*-coding:utf-8 -*-
import numpy as np

# 函数调用不拷贝数组
def change_shape(a):
    a.resize((4, 3))


a = np.arange(12)
print(a.shape)
a.shape = (3, 4)
print(a)
change_shape(a)
print(a)