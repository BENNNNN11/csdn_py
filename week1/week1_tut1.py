#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-22 23:48
# @Author : XXX
# @Site : 
# @File : week1_tut1.py
# @Software: PyCharm

import os

################## 文件读取 ######################

# python 内置的文件读写操作
# OS模块进行文件和文件夹操作
# OS模块进行路径操作

# 按照字符读取文件
f = open('./a.txt', 'r')
data = f.read(3)  # 3 bytes
print(data)
f.close()

# 按照行读取文件
f = open('./a.txt', 'r')
data = f.readline()
while len(data)>0:
    print(data)
    data = f.readline()
f.close()

print('='*60)


################## 文件写入 ######################
f = open('./b.txt', 'w')
f.write('hello python\n')
a = ['hello, java\n','hello, php\n','hello, c++\n']
f.writelines(a)
f.close()


################## 文件复制 ######################
def copy_file(file1, file2):
    '''
    文件复制函数
    :param file1:
    :param file2:
    :return:
    '''
    # 打开源文件和目标文件

    f1 = open(file1, 'rb')
    f2 = open(file2, 'wb')
    # 循环读取写入， 实现复制内容
    data = f1.readline()
    while len(data) > 0:
        f2.write(data)
        data = f1.readline()
    f1.close()
    f2.close()


copy_file('./b.txt', './c.txt')


# 通过os模块实现目录复制函数

def copy_path(dir1, dir2):
    # 获取被复制目录中的所有文件信息
    dlist = os.listdir(dir1)

    # 创建新目录
    os.mkdir(dir2)

    # 便利所有文件，并执行文件复制
    for f in dlist: #为遍历的文件添加目录路径
        file1 = os.path.join(dir1, f)  # 源文件
        file2 = os.path.join(dir2, f)  # 目标文件
        # 如果是文件，直接复制
        if os.path.isfile(file1):
            copy_file(file1, file2)
        # 如果是目录，递归
        if os.path.isdir(file1):
            copy_path(file1, file2)
