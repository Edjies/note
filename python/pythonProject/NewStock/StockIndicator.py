# -*-coding:utf-8 -*-
import talib
import requests
import numpy
from StockConfig import *
from StockIO import *

"""
StockIndicator used for confirm price movement
"""

def kd(kline, n_rsv, n_k, n_d):
    rsv = [0] * kline.shape[0]
    k = [0] * len(rsv)
    d = [0] * len(rsv)
    open = kline[:, 1].astype(np.float)
    close = kline[:, 2].astype(np.float)
    high = kline[:, 3].astype(np.float)
    low = kline[:, 4].astype(np.float)

    if len(rsv) < n_rsv:
        return -1, -1

    for i in range(0, close.shape[0]):
        if i < n_rsv - 1:
            rsv[i] = 0
        else:
            start = i - n_rsv + 1
            end = i + 1
            rsv[i] = (close[i] - np.min(low[start:end])) / (np.max(high[start:end]) - np.min(low[start:end])) * 100

    for index, i in enumerate(rsv):
        if index != 0:
            k[index] = 1/3.0*rsv[index] + 2/3.0*k[index-1]    # 计算平滑移动平均线

    for index, i in enumerate(k):
        if index != 0:
            d[index] = 1/3.0*k[index] + 2/3.0*d[index-1]      # 计算平滑移动平均线

    return k, d


def macd(kline, fastperiod=12, slowperiod=26, signalperiod=9):
    """
    :param kline:
    :return:macd   (nparray)
            macdsignal   (nparray)
            macdhist    (nparray)
    """
    close = kline[:, 2].astype(np.float)
    return talib.MACD(close, fastperiod=fastperiod, slowperiod=slowperiod, signalperiod=signalperiod)


def t_sma():
    data = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    print(talib.SMA(data, timeperiod=3))


def findX(stock_list, kline_type=kline_type_day):
    """
    :param stock_list: list<Stock>
    :param kline_type:
    :return: list<Stock>
    """
    print('findX(stock_list)')
    result = []
    for stock in stock_list:
        k, d = kd(get_kline(stock.stock_code, kline_type), 9, 3, 3)
        if k != -1 and d != -1 and len(k) > 7:
            if d[-3] > k[-3] and k[-2] > d[-2]:
                result.append(stock)
    return result




def query_report(stock_pool):
    reports = []
    codes = ''
    for stock in stock_pool:
        code = stock.stock_code
        if code.startswith('6'):
            code = '0' + code
        else:
            code = '1' + code
        codes = codes + code + ','

    url = 'http://api.money.126.net/data/feed/{}'.format(codes)[:-1]
    print(url)
    r = requests.get(url)
    text = r.text[len('_ntes_quote_callback('): -2]
    print(text)
    json_obj = json.loads(text)
    for key in json_obj.keys():
        item_obj = json_obj[key]
        try:
            reports.append((item_obj['code'][1:], item_obj['price'], item_obj['updown'], item_obj['percent'] * 100))
        except Exception as e:
            print(e)

    reports.sort(key=lambda x:x[3])

    print("%-10s %8s %8s %8s" % ('code', 'price', 'chg', 'chg_per'))
    for report in reports:
        print("%-10s %8.2f %8.2f %8.2f" % (report[0], report[1], report[2], report[3]))


#k, d = kd2(get_kline("601611", kline_type_day), 9, 3, 3)
#k1, d1 = kd(get_kline("000005", kline_type_day))
#print(k[:])
#print(d[:])
# macd,macdsignal,macdhist = macd(get_kline('601611', kline_type_day))
# print(macdhist*2)
# print(macd)
# print(macdsignal)

