# -*-coding:utf-8 -*-
import StockIndicator
import StockReporter
import StockFilter
import StockIO
import StockConfig
import numpy as np


#StockReporter.query_report(StockFilter.find_kdj_x('sha', kline_type=StockConfig.kline_type_day))
stock_list = StockFilter.find_kdj_jx('sha', kline_type=StockConfig.kline_type_day, x_position=-1, about=True)
stock_result = []
for stock in stock_list:
    kline = StockIO.get_kline(stock.stock_code, StockConfig.kline_type_week)
    close = kline[:, 2].astype(np.float)
    sma5 = StockIndicator.sma(kline, 5)
    if close[-1] > sma5[0][-1]:
        stock_result.append(stock)

print(stock_result)
StockReporter.query_report(stock_result)
# print(len(stock_list))
# stock_list_1 = []
# for stock in stock_list:
#     if not stock.stock_code.startswith('300'):
#         stock_list_1.append(stock)
# StockReporter.query_report(stock_list_1)
#stock_list = StockFilter.find_kdj_x('sza', kline_type=StockConfig.kline_type_day)
#print(len(
# stock_list))
#StockReporter.query_report(stock_list)

#stock_list = StockFilter.find_trend_up('sha', StockConfig.kline_type_day)
#print(stock_list)
