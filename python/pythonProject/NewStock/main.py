# -*-coding:utf-8 -*-
import StockIndicator
import StockReporter
import StockFilter
import StockIO
import StockConfig


#StockReporter.query_report(StockFilter.find_kdj_x('sha', kline_type=StockConfig.kline_type_day))
StockReporter.query_report(StockFilter.find_kdj_sx('sha', kline_type=StockConfig.kline_type_day))