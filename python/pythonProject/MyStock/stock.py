# -*-coding:utf-8 -*-
import optparse
import requests
import json
import numpy as np
import StockPool as sp

__author__ = 'hubble'

const_sh = 0
const_sz = 1

const_kline_fs = 'fs'
const_kline_day = 'day'
const_kline_week = 'week'
const_kline_month = 'month'


class Kline(object):
    def __init__(self):
        self.stock_name = ''
        self.stock_code = ''
        self.stock_type = ''
        self.kline_type = const_kline_day




def model1(kline):
    closes = kline.item[:, 2].astype(np.float)  # 切分取矩阵的第三列 然后转为 浮点数， 得到历史收盘价列表
    print(closes.max())  # 获取历史最高收盘价
    print(closes.min())  # 获取历史最低收盘价
    print(closes[-1])    # 获取今日收盘价
    return True

# get kline data
def get_kline(code):
    if code.startswith('6'):
        code = '0' + code
    else:
        code = '1' + code
    print("start analysis {}".format(code))
    url = "http://img1.money.126.net/data/hs/kline/day/history/{}/{}.json".format('2016', code)
    r = requests.get(url)
    json_obj = json.loads(r.text)
    kline_data = Kline()
    kline_data.stock_name = json_obj['name']
    kline_data.stock_code = json_obj['symbol']
    kline_data.kline_type = const_kline_day
    kline_data.item = np.array(json_obj['data'])
    print(kline_data.item)


    return kline_data



# 程序主入口
if __name__ == '__main__':
    # 处理命令行参数
    args_parser = optparse.OptionParser(description="Query the stock's value.", usage="%prog [-s] [-d] [-m] [-p]", version="%prog 1.0")
    args_parser.add_option('-s', '--sort', help='根据查询结果排序', type=str)
    args_parser.add_option('-d', '--hide', help='隐藏某些字段', type=str)
    args_parser.add_option('-m', '--model', help='选择一种模型处理', type=str)
    args_parser.add_option('-p', '--pool', help='选择池', type=str)
    (options, args) = args_parser.parse_args()
    kline = get_kline('600868')
    print('#'*10)
    model1(kline)









