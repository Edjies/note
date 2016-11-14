# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.figure as figure
'''
:param num 	1   number of figure
:param figsize 	figure.figsize 	figure size in in inches (width, height)
:param dpi 	figure.dpi 	resolution in dots per inch
:param facecolor 	figure.facecolor 	color of the drawing background
:param edgecolor 	figure.edgecolor 	color of edge around the drawing background
:param frameon 	True 	draw figure frame or not
'''
X = np.linspace(-np.pi, np.pi, 256,endpoint=True)
C,S = np.cos(X), np.sin(X)
plt.figure(1, edgecolor='blue')
plt.figure(1)
plt.plot(X, C)
plt.plot(X, S)
plt.show()
