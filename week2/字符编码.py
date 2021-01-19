#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-27 00:16
# @Author : XXX
# @Site : 
# @File : 字符编码.py
# @Software: PyCharm

'''
    字符编码
'''

# 字符编码类型
# 字符串编码转换
# 字符编码类型：1.ASCII码
#               2.GB
#               3.Unicode：定长
#               4.utf8
'''
    字节和字符：
'''
print(ord('A'))
print(ord('我'))
print(chr(66))

print(chr(25106))

x=b'asd'
print(x)

print('你好'.encode('utf-8'))

print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'))


