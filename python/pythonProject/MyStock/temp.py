# -*-coding:utf-8 -*-
import os
# 重命名
cur_dir = 'kline/day'

for parents, dirs, files in os.walk(cur_dir):
    for file in files:
        file_name = file
        new_name = file[1:]
        os.rename('{}/{}'.format(cur_dir, file), '{}/{}'.format(cur_dir, new_name))



