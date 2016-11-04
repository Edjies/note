# -*-coding:utf-8 -*-
import requests
import json
import os
__author__ = 'hubble'
sina_node_sh_a = 'sh_a'
sina_node_sz_a = 'sz_a'

stock_pool_sh_a = 'sha'
stock_pool_sz_a = 'sza'

stock_list = []


# 获取股票池数据, 该方法依赖于新浪股票API接口
def get_code_group(node, page):
    print('start load {} page'.format(str(page)))
    url = "http://gu.sina.cn/hq/api/openapi.php/Wap_Market_Center.getHQNodeData?" \
          "num=40&sort=changepercent&asc=0&_s_r_a=init&node={node}&page={page}&dpc=1" \
          .format(node=node, page=page)
    r = requests.get(url)
    # 解析数据
    jsonObj = json.loads(r.text)
    for item in jsonObj['result']['data']['data']:
        stock_list.append((item['code'], item['name']))

    size = jsonObj['result']['data']['status']['pagetatol']
    if page < size:
        get_code_group(node, page + 1)
    return stock_list


# 保存股票池数据
def write_stock_pool(stock_pool, l_stock_list):
    l_stock_list.sort(key=lambda x:x[0])    # 对数据进行排序
    if not os.path.exists('Pool'):
        os.mkdir('Pool')
    f = open('Pool/{}'.format(stock_pool), 'w', encoding='utf-8')
    for stock in l_stock_list:
        f.write("{},{}\n".format(stock[0], stock[1]))
    f.close()


# 读取股票池数据
def read_stock_pool(stock_pool):
    l_stock_list = []
    if not os.path.exists('Pool/{}'.format(stock_pool)):
        return []
    f = open('Pool/{}'.format(stock_pool), 'r', encoding='utf-8')
    for stock in f:
        stock = stock.strip('\n')
        if stock != '':
            l_stock_list.append(stock.split(','))
    print(l_stock_list)
    return l_stock_list


# 股票池去重
def filter(l_stock_list):
    r_stock_list = []
    for stock in l_stock_list:
        if stock not in r_stock_list:
            r_stock_list.append(stock)
    print(r_stock_list)
    return r_stock_list
# write_stock_pool(stock_pool_sh_a, get_code_group(sina_node_sh_a, 1))
# write_stock_pool(stock_pool_sz_a, get_code_group(sina_node_sz_a, 1))
# read_stock_pool(stock_pool_sh_a)
# write_stock_pool(stock_pool_sh_a, filter(read_stock_pool(stock_pool_sh_a)))




