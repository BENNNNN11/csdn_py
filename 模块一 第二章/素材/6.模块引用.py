#!/usr/bin/env python3
# -*- coding:utf-8 -*-
'说明模块用途的地方'
__author__ = 'yh'

def test():
    print('test()调用成功')

if __name__ == '__main__':
    test()


from Test_Package.my1 import my1_test

my1_test()