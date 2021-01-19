#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-23 02:52
# @Author : XXX
# @Site : 
# @File : Q2.py
# @Software: PyCharm
# 使用文件和目录操作，定义一个统计指定目录大小的函数
import os


def dir_size(dir):
    count = 0
    dir_size_rec(dir, count)
    print('{} files are found.'.format(count))


def dir_size_rec(dir, count):

    # 获取被复制目录中的所有文件信息
    dir_list = os.listdir(dir)

    # 遍历所有文件
    for f in dir_list:  # 为遍历的文件添加目录路径
        file1 = os.path.join(dir, f)

        # 如果是文件，计数器加1
        if os.path.isfile(file1):
            count += 1

        # 如果是目录，递归
        if os.path.isdir(file1):
            dir_size_rec(file1, count)