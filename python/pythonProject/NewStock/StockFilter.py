# -*-coding:utf-8 -*-
import StockIndicator
import StockIO


def find_kdj_x(stock_pool, kline_type):
    result = []
    stock_list = StockIO.get_stock(stock_pool)
    for stock in stock_list:
        k, d = StockIndicator.kd(StockIO.get_kline(stock.stock_code, kline_type), 9, 3, 3)
        if k != -1 and d != -1 and len(k) > 7:
            if d[-3] > k[-3] and k[-2] > d[-2]:
                result.append(stock)
    return result


def find_macd_x(stock_pool, kline_type, x_position = -1):
    result = []
    stock_list = StockIO.get_stock(stock_pool)
    for stock in stock_list:
        macd, macdsignal, macdhist = StockIndicator.macd(StockIO.get_kline(stock.stock_code, kline_type))
        if macd.shape[0] - 1 > abs(x_position):
            if macdsignal[x_position - 1] > macd[x_position - 1] and macd[x_position] > macdsignal[x_position]:
                result.append(stock)
    return result

