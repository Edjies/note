# -*-coding:utf-8 -*-
__author__ = 'hubble'
import json
import numpy as np

# json 解析与生成
f = open('testDir/jsonFile', 'r', encoding='utf-8')
text = f.readline()
f.close()
json_obj = json.loads(text)  # 返回一个dict对象
print(json_obj.keys())         # 打印key值

data = {}
data['data'] = json_obj['data']#  解析
data['name'] = json_obj['name']
data['symbol'] = json_obj['symbol']
data['data'].append(["20161027", 18.23, 17.8, 18.28, 17.55, 43334434, 10.07]) # 添加新数据

json_str = json.dumps(data)    # 生成
print(json_str)

# dfsdf






