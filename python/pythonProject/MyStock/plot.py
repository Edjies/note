# -*-coding:utf-8 -*-
import matplotlib.pyplot as plt
import KLinePool as kp
import json
import numpy as np


def plot_weekly_close(stock_list):
    size = len(stock_list)
    for stock in stock_list:
        jsonObj = json.loads(kp.read_kline(kp.const_file_dir_day, stock[0]))
        item = np.array(jsonObj['data'])  # 取出数据
        closes = item[:, 2].astype(np.float)  # 取出close 数据
        print(len(closes))
        plt.title(stock[0])
        plt.plot(closes)
        plt.show()
plot_weekly_close([['601989','']])