# -*-coding:utf-8 -*-
import StockIO
import StockConfig
import numpy as np
def down(stock_list, kline_type, start=-5, end=-1, output=False):
    result = []
    for stock in stock_list:
        kline = StockIO.get_kline(stock.stock_code, kline_type)
        print(kline.shape)
        if kline.shape[0] > abs(start):
            close = kline[:, 2].astype(np.float)
            maxHigh = np.max(kline[:, 3].astype(np.float)[start:end])
            minLow = np.min(kline[:, 4].astype(np.float)[start:end])
            if close[-1] < maxHigh:
                result.append([stock.stock_code, stock.stock_name, (maxHigh - minLow)/minLow * 100])

    result = sorted(result, key=lambda item:item[2])
    print(result)

down(StockIO.get_stock('sha'), StockConfig.kline_type_day)

