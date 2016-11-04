# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


# plot用于绘制图像
def plt1():
    plt.plot([1, 2, 3, 4])   # y value
    plt.ylabel('some values')
    plt.show()

    plt.plot([1, 2, 3, 4], [2, 3, 4, 5])  # x, y value
    plt.ylabel('y value')
    plt.xlabel('x value')
    plt.show()


def plt2():
    plt.plot([1, 2, 3, 4], [2, 3, 4, 5])   # x, y value
    plt.ylabel('y value')
    plt.xlabel('x value')
    plt.show()


# 将多个图绘制到一个平面
# subplot 指定整个平面中的某一块用来绘制， 第一个代表行数， 第二个代表列数， 第三个代表当前图在平面中的位置，从左到右，从上到下，从1开始
# 最后调用show()方法
def multiPlot():
    p1 = np.arange(1, 10)
    p2 = np.arange(1, 10, 0.02)

    plt.subplot(211)
    plt.plot(p1, p1**2, 'bo')

    plt.subplot(212)
    plt.plot(p2, np.cos(2*np.pi*p2), 'r--')
    plt.show()


# 同时绘制多张图片
def multiFigure():
    plt.figure(1)  # the first figure
    plt.subplot(211)  # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212)  # the second subplot in the first figure
    plt.plot([4, 5, 6])

    plt.figure(2)  # a second figure
    plt.plot([4, 5, 6])  # creates a subplot(111) by default

    plt.figure(1)  # figure 1 current; subplot(212) still current
    plt.subplot(211)  # make subplot(211) in figure1 current
    plt.title('Easy as 1, 2, 3')  # subplot 211 title

    plt.subplot(212)
    plt.title("Easy as 4, 5, 6")
    plt.plot([1, 2, 3], 'b')
    plt.show()

plt1()
#plt2()
#multiPlot()
#multiFigure()