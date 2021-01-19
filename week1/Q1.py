#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-23 01:47
# @Author : XXX
# @Site : 
# @File : Q1.py
# @Software: PyCharm
#

######################## Q1 For Loop ########################

for row in range(1,10):
    for col in range(1,row+1):
        print("{}*{}={:<3}".format(col,row,row*col), end=" ")
    print('')
print('='*70)
print('')
for row in range(9,0,-1):
    for col in range(1,row+1):
        print("{}*{}={:<3}".format(col,row,row*col), end=" ")
    print('')

for row in range(1,10):
    print(' ' * 8 * (9-row), end='')
    for col in range(row, 0, -1):
        print("{}*{}={:<3}".format(col,row, col*row), end=" ")
    print('')
print('='*70)
print('')
for row in range(1,10):
    print(' ' * 8 * (row-1), end='')
    for col in range(10-row, 0, -1):
        print("{}*{}={:<3}".format(col, 10-row, (10-row)*col), end=" ")
    print('')



######################## Q1 while Loop ########################

row = 1
while row < 10:
    col = 1
    while col <= row:
        print("{}*{}={:<3}".format(col, row, col * row), end=" ")
        col += 1
    print('')
    row+=1
print('='*70)
print('')


row = 9
while row > 0:
    col = 1
    while col <= row:
        print("{}*{}={:<3}".format(col, row, col * row), end=" ")
        col += 1
    print('')
    row-=1
print('='*70)
print('')


row = 1
while row < 10:
    col = row
    print(' '*8*(9-row),end='')
    while 0 < col <= row:
        print("{}*{}={:<3}".format(col, row, col * row), end=" ")
        col -= 1
    print('')
    row+=1
print('='*70)
print('')

row = 9
while row > 0:
    col = row
    print(' '*8*(9-row),end='')
    while 0 < col <= row:
        print("{}*{}={:<3}".format(col, row, col * row), end=" ")
        col -= 1
    print('')
    row-=1
print('='*70)
print('')