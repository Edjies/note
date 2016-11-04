# -*-coding:utf-8 -*-
import requests
import json

# now, chg, chg_per,
def query_report(stock_pool):
    reports = []
    codes = ''
    for stock in stock_pool:
        code = stock[0]
        if code.startswith('6'):
            code = '0' + code
        else:
            code = '1' + code
        codes = codes + code + ','

    url = 'http://api.money.126.net/data/feed/{}'.format(codes)[:-1]
    print(url)
    r = requests.get(url)
    text = r.text[len('_ntes_quote_callback('): -2]
    print(text)
    json_obj = json.loads(text)
    for key in json_obj.keys():
        item_obj = json_obj[key]
        reports.append((item_obj['code'][1:], item_obj['price'], item_obj['updown'], item_obj['percent'] * 100))

    reports.sort(key=lambda x:x[3])

    print("%-10s %8s %8s %8s" % ('code', 'price', 'chg', 'chg_per'))
    for report in reports:
        print("%-10s %8.2f %8.2f %8.2f" % (report[0], report[1], report[2], report[3]))