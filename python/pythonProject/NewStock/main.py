# -*-coding:utf-8 -*-
import StockIndicator
import StockReporter
import StockFilter
import StockIO
import StockConfig


#StockReporter.query_report(StockFilter.find_kdj_x('sha', kline_type=StockConfig.kline_type_day))
stock_list = StockFilter.find_kdj_jx('sha', kline_type=StockConfig.kline_type_day, x_position=-2, k_max=20, period=-8, times=2)
print(len(stock_list))
StockReporter.query_report(stock_list)
#stock_list = StockFilter.find_kdj_x('sza', kline_type=StockConfig.kline_type_day)
#print(len(stock_list))
#StockReporter.query_report(stock_list)
