# -*-coding:utf-8 -*-
__author__ = 'hubble'


# 类方法， 静态方法 和 实例方法
class Test(object):

    def add3(self, a3, b3):
        return a3+b3

    @classmethod
    def add(cls, a1, b1):
        return a1 + b1

    @staticmethod
    def add2(a2, b2):
        return a2 + b2

data = ('ah', 'bh', 'ch')
a, b, c = data  # assign multi value from a tuple
print(a, b, c)  # print multi value

data = ['a', 'b', 'c']
a, b, c = data
print(a, b, c)

#  切片 第一个参数表示从哪开始，第二个参数表示从哪结束， 第三个参数表示切片间隔（负数从最后一个元素开始），
data = [1, 2, 3, 4, 5, 6, 7, 8]
print(data[-2:])

#   __name__ == '__main__'  如果直接执行该文件，则值为true, 作为模块导入时， 值为false