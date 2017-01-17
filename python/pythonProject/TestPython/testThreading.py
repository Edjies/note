from threading import Thread
import time

class Task(Thread):
    def __init__(self, name):
        Thread.__init__(self)
        self.name = name
        pass

    def run(self):
        count = 1
        while(True):
            count += 1
            time.sleep(1)
            print(self.name, ' run:', count)


def testRunThread():
    t1 = Task('task1')
    t2 = Task('task2')
    t3 = Task('task3')
    t1.start()
    t2.start()
    t3.start()







