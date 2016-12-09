# -*-coding:utf-8 -*-
import talib
import requests
import numpy
from StockConfig import *
from StockIO import *

"""
StockIndicator used for confirm price movement
"""


def kd(kline):
    """

    :param kline: nparray<date, open, close, high, low, volume>
    :return:
    """
    # rsv
    # k = (price - L5)/(H5 - L5)
    # d = 100 * ((K1 + k2 + k3) / 3)
    # return
    try:
        k, d = talib.STOCH(kline[:, 3].astype(np.double), kline[:, 4].astype(np.double), kline[:, 2].astype(np.double),
                       fastk_period=9, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    #k, d = talib.STOCHF(kline[:, 3].astype(np.double), kline[:, 4].astype(np.double), kline[:, 2].astype(np.double), fastk_period=9, fastd_period=3, fastd_matype=0)
    except Exception as e:
        return [0, 0], [0, 0]
    return k, d


def findX(stock_list):
    """
    :param stock_list: list<Stock>
    :return: list<Stock>
    """
    result = []
    for stock in stock_list:
        k, d = kd(get_kline(stock.stock_code, kline_type_day))
        if d[-2] > k[-2] and k[-1] > d[-1]:
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


stocks = findX(get_stock('sza'))
print(stocks)
query_report(stocks[20:])