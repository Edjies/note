# -*-coding:utf-8 -*-
import StockIndicator
import StockReporter
import StockFilter
import StockIO
import StockConfig


#StockReporter.query_report(StockFilter.find_kdj_x('sha', kline_type=StockConfig.kline_type_day))
stock_list = StockFilter.find_kdj_x('sha', kline_type=StockConfig.kline_type_day)
stock_list_1 = []
print(len(stock_list))
for stock in stock_list:
    k, d = StockIndicator.kd(StockIO.get_kline(stock.stock_code, StockConfig.kline_type_week))
    k2, d2 = StockIndicator.kd(StockIO.get_kline(stock.stock_code, StockConfig.kline_type_month))
    if k[-1] > d[-1]  and k[-1] > 40 and k[-1] < 60:
        stock_list_1.append(stock)

print(len(stock_list_1))
StockReporter.query_report(stock_list_1)
#stock_list = StockFilter.find_kdj_x('sza', kline_type=StockConfig.kline_type_day)
#print(len(stock_list))
#StockReporter.query_report(stock_list)