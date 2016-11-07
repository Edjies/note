# -*-coding:utf-8 -*-
__author__ = 'hubble'
import json
import requests

# 打印列表元素  重写 __str__方法， print(*list, sep='--')
class StockBase(object):
    def __init__(self, stock_name, stock_code):
        self.stock_name = stock_name
        self.stock_code = stock_code

    def __str__(self):
        return "({},{})".format(self.stock_name, self.stock_code)

stock_list = []
for i in range(10):
    stock_list.append(StockBase("大师傅", "000900"))
print(*stock_list, sep='--')

# 列表排序1
l = [('a', '1'), ('c', '3'), ('d', '4'), ('b', '2')]
l.sort(key=lambda x:x[1])
print(l)

# 切片
data = []
for i in range(1, 9):
    data.append(i)
print(data)
print(data[-28:])

# 相等判断
list1 = [True, False, True]
list2 = [True, False, True]
print("list1 == list2 is {}".format(list1 == list2))
print('list1.equals(list2) is {}'.format(list1 is list))

# 排序
list1 = [1, 4, 2, 3]
print(sorted(list1))
print(sorted(list1, reverse=True))
