# -*-coding:utf-8 -*-
import zipfile
import os


def zip_data(path, zip_name):
    f = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            f.write(os.path.join(dirpath, filename))
    f.close()

zip_data('Pool', 'Pool.zip')
zip_data('kline', 'kline.zip')