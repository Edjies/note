# -*-coding:utf-8 -*-
# hasattr, getattr, delattr, setattr


a = 1

class A(object):
    def __init__(self):
        pass

t = A()
a = 'abc'
b = 's'
if not hasattr(t, a):
    setattr(t, a, 123)

print(t.abc)

print(getattr(t, b, 1234))

delattr(t, a)

print(hasattr(t, a))



