# -*-coding:utf-8 -*-
import os
import requests
import StockPool as sp
import time
import json
__author__ = 'hubble'

const_kline_fs = 'fs'
const_kline_day = 'day'
const_kline_week = 'week'
const_kline_month = 'month'

const_file_dir_day = 'kline/day'
const_file_dir_week = 'kline/week'
const_file_dir_month = 'kline/month'


# get kline data
def get_kline_day(stock_list):
    for stock in stock_list:
        code = stock[0]
        if code.startswith('6'):
            code = '0' + code
        else:
            code = '1' + code

        path = '{}/{}'.format(const_file_dir_day, stock[0])
        if not os.path.exists(path):
            print("开始下载 {} 的日线数据".format(stock[0]))
            url = "http://img1.money.126.net/data/hs/kline/day/history/{}/{}.json".format('2016', code)
            r = requests.get(url)
            save_kline(path, r.text)

def get_kline_week(stock_list):
    for stock in stock_list:
        code = stock[0]
        if code.startswith('6'):
            code = '0' + code
        else:
            code = '1' + code
        path = '{}/{}'.format(const_file_dir_week, stock[0])
        headers = {'Host': 'img1.money.126.net',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Connection': 'keep-alive',
                   'Cookie': '__gads=ID=ffd1eb4604430ca7:T=1477876444:S=ALNI_MbNRLnb9W9zEb2bbqijtExB7fri0g',
                   'Upgrade-Insecure-Requests': '1'}
        if not os.path.exists(path):
            print("开始下载{}的周线数据".format(stock[0]))
            url = "http://img1.money.126.net/data/hs/kline/week/history/{}/{}.json".format('2016', code)
            r = requests.get(url, headers=headers)
            save_kline(path, r.text)



def save_kline(path, text):
    f = open(path, 'w', encoding='utf-8')
    f.write(text)
    f.close()


def read_kline_day(stock_code):
    f = open('{}/{}'.format(const_file_dir_day, stock_code), 'r', encoding='utf-8')
    text = f.readline()
    f.close()
    return text

def read_kline(dir, stock_code):
    f = open('{}/{}'.format(dir, stock_code), 'r', encoding='utf-8')
    text = f.readline()
    f.close()
    return text

def upate_kline_day(node, page):

    url = "http://gu.sina.cn/hq/api/openapi.php/Wap_Market_Center.getHQNodeData?" \
          "num=40&sort=changepercent&asc=0&_s_r_a=init&node={node}&page={page}&dpc=1" \
        .format(node=node, page=page)

    headers = {'Host': 'gu.sina.cn',
               'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Connection': 'keep-alive',
               'Cookie': 'WEB2_APACHE2_GD=d7e1edf57b5ab02dab75ffb90d6d03d4',
               'Upgrade-Insecure-Requests': '1'}
    r = requests.get(url, headers=headers)
    jsonObj = json.loads(r.text)
    date = jsonObj['result']['data']['status']['date']
    for item in jsonObj['result']['data']['data']:
        # 最新数据
        new_item = [date.replace('-', ''), float(item['open']), float(item['trade']), float(item['high']), float(item['low']), item['volume'], float(item['changepercent'])]
        # 旧数据
        code = item['code']
        print('正在更新{}'.format(code))
        if os.path.exists('{}/{}'.format(const_file_dir_day, code)):
            f = open('{}/{}'.format(const_file_dir_day, code), 'r', encoding='utf-8')
            text = f.readline()
            f.close()
            old_obj = json.loads(text)
            data = {}
            data['data'] = old_obj['data']  # 解析
            data['name'] = old_obj['name']
            data['symbol'] = old_obj['symbol']
            old_item = data['data'][-1]
            if old_item[0] == new_item[0]:
                print('update', new_item, old_item)
                data['data'][-1] = new_item
                json_str = json.dumps(data)  # 生成
                save_kline('{}/{}'.format(const_file_dir_day, code), json_str)
            else:
                print('append', new_item, old_item)
                data['data'].append(new_item)
                json_str = json.dumps(data)  # 生成
                save_kline('{}/{}'.format(const_file_dir_day, code), json_str)
                # data['data'].append()
    size = jsonObj['result']['data']['status']['pagetatol']
    if page < size:
        upate_kline_day(node, page + 1)

if __name__ == '__main__':
    '''
    if not os.path.exists(const_file_dir_day):
            os.makedirs(const_file_dir_day)
    stock_list = sp.read_stock_pool(sp.stock_pool_sh_a)
    get_kline_day(stock_list)
    '''

    upate_kline_day('sh_a', 1)
    upate_kline_day('sz_a', 1)

    '''
    stock_list = sp.read_stock_pool(sp.stock_pool_sh_a)
    get_kline_week(stock_list)
    '''


