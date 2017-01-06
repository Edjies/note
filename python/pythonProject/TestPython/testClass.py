# -*-coding:utf-8 -*-
class Person:
    def __init__(self, name, age):
        self._name = name
        self.age = age

    @property
    def name(self):
        print('get name')
        return self._name

    @name.setter
    def name(self, value):
        print('set name')
        self._name = value


class ClassA(object):
    static_item_a = 'ClassA'    # 类变量， 但是 每个实例仍然有自己的成员变量， 区别在于如何访问

    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

a1 = ClassA(field1='1', field2='2')
a1.static_item_a = 'ClassA1'

a2 = ClassA(field1='3', field2='4')
a3 = ClassA(a=1, b=2)

print(ClassA.static_item_a, a2.static_item_a)
print(a1.field1, a2.field1)
b = ClassA
print(b)

