# -*-coding:utf-8 -*-
import numpy as np
import json
import os
import matplotlib.pyplot as plt
import KLinePool as kp

# 上涨势
def uptrend():
    return


# 下跌势
def downtrend():
    return


# 平势
def sideways():
    return


def extreme_line(kline_data=np.array([]), noise_factor=1):
    '''

    :param kline_data:  k线数据
    :param noise_factor: 噪音因子, 比如factor=1代表所有的数据都为有效数据， factor=2代表至少存在两个点的趋势才代表极值点的形成
    :return: 各个极值点的数据
    '''
    closes = kline_data[:, 2].astype(np.float)  # 取出close 数据
    extremes = []
    for i in range(noise_factor, len(closes.flat) - noise_factor):
        # i左边的序列成递增状态， i右边的序列成递减状态，则i为极大值
        # i左边的序列成递减状态， i右边的序列成递增状态，则为极小值
        left = closes[i - noise_factor:i + 1]
        right = closes[i:i + noise_factor + 1]
        '''
        if (sorted(left) == left).all() and (sorted(right, reverse=True) == right).all():   # 极大值
            extremes.append(kline_data[i])
        elif (sorted(left, reverse=True) == left).all() and (sorted(right) == right).all():  # 极小值
            extremes.append(kline_data[i])
        '''

        '''
        if left.min() == closes[i - noise_factor] and left.max() == closes[i] and right.max() == closes[i] and right.min() == closes[i + noise_factor]:
            extremes.append(kline_data[i])
        elif left.max() == closes[i - noise_factor] and left.min() == closes[i] and right.min() == closes[i] and right.max() == closes[i + noise_factor]:
            extremes.append(kline_data[i])
        '''
        all = closes[i - noise_factor: i +  noise_factor + 1]
        if all.min() == closes[i] or all.max() == closes[i]:
            extremes.append(kline_data[i])

    return extremes


def main(stock_code):
    if os.path.exists('{}/{}'.format(kp.const_file_dir_week, stock_code)):
        json_obj = json.loads(kp.read_kline(kp.const_file_dir_week, stock_code))
        item = np.array(json_obj['data'])  # 取出数据
        extrems = extreme_line(item, noise_factor=1)
        plt.plot(np.array(extrems)[:, 2].astype(np.float))
        plt.show()
    return


if __name__ == '__main__':
    main('000878')


