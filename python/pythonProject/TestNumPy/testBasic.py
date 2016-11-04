import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)

a = np.arange(20)
print(a.ndim)

a = a.reshape(4, 5)
print(a)
print(a.ndim)
print(a.shape)
print(a.itemsize)
print(a.data)

# 创建np数组
nparr1 = np.array(([2,4],[1,2],[2,3]), dtype=complex)
nparr2 = np.array([[1,2],[3,4],[5,6]], dtype=int)
nparr3 = np.arange(3, 21, 2)
zero = np.zeros((3,4,5))
one = np.ones((3,4))
print(nparr1)
print(nparr2)
print(nparr3)
print(zero)
print(one)

# 基本操作
nparr1 = np.arange(4)
nparr2 = np.arange(5, 9, 1)
print(nparr1 + nparr2)
print(nparr1 * nparr2)
print(np.sin(nparr1))
print(2 > nparr1)

# 操作某一维度的元素
nparr1 = np.random.random((3,4))
print(nparr1)
print(nparr1.sum(axis=0))
print(nparr1.min(axis=1))
print(nparr1.min())

# index, slice, iterator
def func(x, y):
    return x + y

nparr1 = np.fromfunction(func, (4,5), dtype=int)
print(nparr1)

# 行迭代器
for row in nparr1:
    print(row)
# 元素迭代器
for e in nparr1.flat:
    print(e)
# 切分
print(nparr1[:1])  # 0-1行的所有列， 缺省代表所有
print(nparr1[1:, 1]) # 第一列以及从第一行开始的所有行

# 单维的矩阵可以当做列表

# 改变形状
nparr1 = np.floor(10 * np.random.random((4,5)))
print(nparr1)
nparr1.reshape(5,4)
print(nparr1)
nparr1.resize((5,4))
print(nparr1)

#











