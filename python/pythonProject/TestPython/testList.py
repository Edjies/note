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
