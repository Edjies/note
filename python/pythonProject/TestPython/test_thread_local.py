# -*- coding:utf-8 -*-

from threading import Thread, local

storage = local()   # 以线程ID保存多份状态字典, 一个线程对对象的修改不会影响另一个线程, 相当于每个线程对应一个 storage对象。 优点： 同一个对象在多个线程下做到状态隔离

class Task(Thread):
    def __init__(self):
        Thread.__init__(self)
        pass

    def run(self):
        storage.count = 5
        print(storage.count)

    def printCount(self):
        print(storage.count)


storage.count = 7
t1 = Task()
t1.start()
print(storage.count)
t1.printCount()