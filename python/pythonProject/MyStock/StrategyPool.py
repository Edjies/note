# -*-coding:utf-8 -*-
__author__ = 'hubble'
import os
import numpy as np
import plot
import StockPool as sp
import KLinePool as kp
import json
import RealTimeData


const_file_dir = 'result'


# 找出前三天up,后两天down的
def filter1(stock_pool):
    if not os.path.exists(const_file_dir):
        os.makedirs(const_file_dir)

    result_pool = []

    stock_list = sp.read_stock_pool(stock_pool)
    for stock in stock_list:
        if os.path.exists('{}/{}'.format(kp.const_file_dir_day, stock[0])):
            jsonObj = json.loads(kp.read_kline_day(stock[0]))
            item = np.array(jsonObj['data'])  # 取出数据
            closes = item[:, 2].astype(np.float)  # 取出close 数据
            opens = item[:, 1].astype(np.float)  # 取出 open 数据

            chg = opens - closes  # 计算chg
            chg = chg[-5:]  # 取出最后五天的chg数据


            # 找出符合条件的
            if len(chg) >= 5:   # 过滤掉new stock
                anchor = np.array([1, 1, 1, -1, -1]) > 0
                if(anchor == (chg <= 0)).all():
                    # print('{}:{}'.format(stock[0], chg), closes[-1], mean)
                    result_pool.append(stock)
    #RealTimeData.query_report(result_pool)
    plot.plot_weekly_close(result_pool)


# 最近两个个月处于——状态的
def filter2(stock_pool):
    if not os.path.exists(const_file_dir):
        os.makedirs(const_file_dir)

    result_pool = []
    stock_list = sp.read_stock_pool(stock_pool)
    for stock in stock_list:
        if os.path.exists('{}/{}'.format(kp.const_file_dir_day, stock[0])):
            jsonObj = json.loads(kp.read_kline_day(stock[0]))
            item = np.array(jsonObj['data'])  # 取出数据
            closes = item[:, 2].astype(np.float)
            closes = closes[-50:]
            mean = closes.mean()
            max = closes.max()
            min = closes.min()
            min10 = closes[-10:].min()
            up = (max - mean) / mean *100
            down = (mean - min) / mean * 100
            if up < 4 and down < 4 and closes[-1] < mean:
                # print('{}:up:{},down:{},mean:{}'.format(stock, up, down, mean))
                result_pool.append(stock)
    RealTimeData.query_report(result_pool)


def filter3(stock_pool):
    if not os.path.exists(const_file_dir):
        os.makedirs(const_file_dir)

    result_pool = []
    stock_list = sp.read_stock_pool(stock_pool)
    for stock in stock_list:
        if os.path.exists('{}/{}'.format(kp.const_file_dir_day, stock[0])):
            json_obj = json.loads(kp.read_kline_day(stock[0]))
            item = np.array(json_obj['data'])
            closes = item[:, 2].astype(np.float)  # 取出close 数据
            opens = item[:, 1].astype(np.float)  # 取出 open 数据
            shares = item[:, 5].astype(np.int) # 取出量
            chg = closes - opens  # 计算chg
            if len(chg) > 5:
                chg = chg[-4:]
                anchor = np.array([-1, -1, 1, 1]) > 0
                if (anchor == (chg > 0)).all():
                    if shares[-4] > shares[-3] and shares[-2] < shares[-1]:
                        # print('{}:{}'.format(stock[0], chg))
                        result_pool.append(stock)
    RealTimeData.query_report(result_pool)

def filter3(stock_pool):
    if not os.path.exists(const_file_dir):
        os.makedirs(const_file_dir)

    result_pool = []
    stock_list = sp.read_stock_pool(stock_pool)



filter1(sp.stock_pool_sh_a)





