# -*-coding:utf-8 -*-
import StockIndicator
import StockIO


def find_kdj_x(stock_pool, kline_type, n_rsv=9):
    """
    kdj金叉
    :param stock_pool: name
    :param kline_type:
    :param n_rsv:
    :return:  stock_list
    """
    result = []
    stock_list = StockIO.get_stock(stock_pool)
    for stock in stock_list:
        k, d = StockIndicator.kd(StockIO.get_kline(stock.stock_code, kline_type), n_rsv)
        if k.shape[0] > n_rsv:
            if d[-3] > k[-3] and k[-2] > d[-2] and d[-2] > d[-3] and k[-2] > k[-3]:
                result.append(stock)
    return result


def find_kdj_sx(stock_pool, kline_type, n_rsv=9):
    """
    kdj死叉
    :param stock_pool: name
    :param kline_type:
    :param n_rsv:
    :return:  stock_list
    """
    result = []
    stock_list = StockIO.get_stock(stock_pool)
    for stock in stock_list:
        k, d = StockIndicator.kd(StockIO.get_kline(stock.stock_code, kline_type), n_rsv)
        if k.shape[0] > n_rsv:
            if d[-3] < k[-3] and k[-2] < d[-2] and d[-2] < d[-3] and k[-2] < k[-3]:
                result.append(stock)
    return result



def find_macd_x(stock_pool, kline_type, x_position = -1):
    """
    macd金叉
    :param stock_pool:
    :param kline_type:
    :param x_position:
    :return: stock_list
    """
    result = []
    stock_list = StockIO.get_stock(stock_pool)
    for stock in stock_list:
        macd, macdsignal, macdhist = StockIndicator.macd(StockIO.get_kline(stock.stock_code, kline_type))
        if macd.shape[0] - 1 > abs(x_position):
            if macdsignal[x_position - 1] > macd[x_position - 1] and macd[x_position] > macdsignal[x_position] and macd[x_position] > macd[x_position - 1] and macdsignal[x_position] > macdsignal[x_position - 1]:
                result.append(stock)
    return result


def find_macd_sx(stock_pool, kline_type, x_position = -1):
    """
    macd死叉
    :param stock_pool:
    :param kline_type:
    :param x_position:  死叉发生点
    :return: stock_list
    """
    result = []
    stock_list = StockIO.get_stock(stock_pool)
    for stock in stock_list:
        macd, macdsignal, macdhist = StockIndicator.macd(StockIO.get_kline(stock.stock_code, kline_type))
        if macd.shape[0] - 1 > abs(x_position):
            if macdsignal[x_position - 1] < macd[x_position - 1] and macd[x_position] < macdsignal[x_position] and macd[x_position] < macd[x_position - 1] and macdsignal[x_position] < macdsignal[x_position - 1]:
                result.append(stock)
    return result


def intersection(l1, l2):
    """
    取两个列表的交集
    :param l1:
    :param l2:
    :return:
    """
    return [x for x in l1 if x in l2]



