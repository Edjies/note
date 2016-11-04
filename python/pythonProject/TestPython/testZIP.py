# -*-coding:utf-8 -*-
import zipfile
import os

# 压缩文件
path = 'testDir'
f = zipfile.ZipFile('zipfile1.zip', 'w', zipfile.ZIP_DEFLATED)
for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        print(filename)
        f.write(os.path.join(dirpath,filename))
f.close()

# 解压文件
f = zipfile.ZipFile('zipfile1.zip', 'r')
for file in f.namelist():
    f.extract(file, 'testDir')
f.close()