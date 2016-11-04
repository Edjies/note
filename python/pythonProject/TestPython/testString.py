# -*-coding:utf-8 -*-
#  str.format方法
print('I\'m {}, my age is {}'.format('panhaobo', '25'))
print('{1}, {0}'.format('a', 'b'))
print('{name}，{age}'.format(age='25' ,name='panhaobo'))
print('#'*40)
print('{}'.format(12))

# str index
code = '600123'
if code.startswith('6'):
    code = '0' + code
else:
    code = '1' + code
print(code)

# split
print('000,123'.split(','))

# replace
print('2016-10-25'.replace('-',''))

# 字符串截取
text='asdk1234fd'
print(text[4:-2])

# 字符串拼接
print('1' + '2' + '3')

# 格式化输出
print('the price is %.2f $'%(1.8934))     # 指定小数点位数
print("%10s %5.2f %6.2f %3.2f"%('0', 1.2342342342, 23.09, 1.23))  # 指定占位符宽度
print("%-10s %-5.2f %-6.2f %-3.2f"%('0', 1.2342342342, 23.09, 1.23))  # 指定对齐方式