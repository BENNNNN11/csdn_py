#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-22 20:51
# @Author : XXX
# @Site : 
# @File : week1.py
# @Software: PyCharm

for row in range(1,10):
    for col in range(1,row+1):
        print("{}*{}={:<2}".format(row,col,row*col), end=" ")
    print('')

print('')
for row in range(9,0,-1):
    for col in range(1,row+1):
        print("{}*{}={:<2}".format(row,col,row*col), end=" ")
    print('')


