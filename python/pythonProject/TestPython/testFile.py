# -*-coding:utf-8 -*-
import os
import sys
# 判断文件是否存在
if not os.path.exists('testDir'):
    os.mkdir('testDir')

# 写文件（会覆盖原有内容）
f = open('testDir/testFile', 'w')
text = ['asdfasdff', 'asdlkfajsldkf']
f.writelines(text)
f.write('123123123')
f.write('\n')             # 写入换行符
f.write('dkfjasodfi')
f.close()

# 写文件（不会覆盖原有内容）
f = open('testDir/testFile', 'a')
f.write('\nhello')
f.close()

# 写utf-8格式的文件
f = open('testDir/testFile2', 'w', encoding='utf-8')
f.write('\n夜里挑灯看剑')
f.close()

# 读文件
f = open('testDir/testFile', 'r')
for line in f:
    line = line.strip('\n')  # 去掉每行的换行符
    print(line)
f.close()

# 读取utf-8文件
f = open('testDir/testFile2', 'r', encoding='utf-8')
for line in f:
    line = line.strip('\n')
    print(line)
f.close()

# 创建单级目录和多级目录
dirs = 'src/main/java'
if os.path.exists(dirs):
    os.makedirs(dirs)

dir = 'res'
if os.path.exists(dir):
    os.mkdir(dir)

# 遍历文件
for parent, dirs, files in os.walk('testDir'):  # 三个变量分别代表当前目录名， 所有子目录列表名， 所有文件列表名
    print(parent)
    for dir in dirs:
        print(dir)
    for file in files:
        print(file)

# 重命名
#os.rename('testDir/testFileR', 'testDir/testFile')

# path
print(os.path.dirname(__file__))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir, 'stock', 'track')))
