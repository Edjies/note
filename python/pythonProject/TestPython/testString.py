# -*-coding:utf-8 -*-
import re
#  str.format方法
# print('I\'m {}, my age is {}'.format('panhaobo', '25'))
# print('{1}, {0}'.format('a', 'b'))
# print('{name}，{age}'.format(age='25' ,name='panhaobo'))
# print('#'*40)
# print('{}'.format(12))
#
# # str index
# code = '600123'
# if code.startswith('6'):
#     code = '0' + code
# else:
#     code = '1' + code
# print(code)
#
# # split
# print('000,123'.split(','))
#
# # replace
# print('2016-10-25'.replace('-',''))
#
# # 字符串截取
# text='asdk1234fd'
# print(text[4:-2])
#
# # 字符串拼接
# print('1' + '2' + '3')
#
# # 格式化输出
# print('the price is %.2f $'%(1.8934))     # 指定小数点位数
# print("%10s %5.2f %6.2f %3.2f"%('0', 1.2342342342, 23.09, 1.23))  # 指定占位符宽度
# print("%-10s %-5.2f %-6.2f %-3.2f"%('0', 1.2342342342, 23.09, 1.23))  # 指定对齐方式

# 字符串分割
def test_split():
    s = 'hello, phb. welcome to shenzhen'
    result = re.split(r'[,.\s]\s*', s)# 使用正则分割字符串
    result2 = re.split(r'(,|\.|\s)\s*', s) # 使用"()"捕获分割串
    result3 = re.split(r'(?:,|\.|\s)\s*', s)  # 使用"(?:...)"不保留分割串
    print(result)
    print(result2)
    print(result3)


#字符串匹配开头或结尾
def test_match():
    s = 'I don\'t know why no one has mentioned this yet'
    print(s.startswith('I'))      # 使用字符串匹配
    print(s.endswith(('t', 'a')))     # 使用可迭代对象匹配


# 正则匹配搜索
def test_re_match():
    s = 'abcdeafdjfadffefabcfesabcde'
    pat = re.compile(r'abc.')
    m = pat.findall(s)
    for ms in m:
        print(ms)
