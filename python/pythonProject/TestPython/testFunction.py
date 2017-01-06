# -*-coding:utf-8 -*-

def testArgs(*timeperiod):
    print(len(timeperiod))
    for i in timeperiod:
        print(i)


def testArgs1(*timeperiod):
    return [x for x in timeperiod]


def testReturn():
    return 1, True

# a, b = testArgs1(1, 2)
# print(a, b)
#
# a, b, c = tuple(x for x in range(3))
# print(a, b, c)
#
# a ,b, c = [1, 2, 3]
# print(a, b, c)

print(testReturn()[1])