#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-01-21 18:55
# @Author : Jiabin Wang
# @Site : 
# @File : Q2.py
# @Software: PyCharm
# @Function: 请设计一个装饰器，它可以作用于任何函数上，打印函数执行时间

import time


def metric(fn):
    def wrapper():
        start_time = time.time()
        fn()
        end_time = time.time()
        print('耗时：{:.4f}s'.format(end_time - start_time))
        return fn(*args, **kw)
    return wrapper


@metric
def run():
    time.sleep(1)
    res = [x ** 2 for x in range(10)]
    print(res)


if __name__ == '__main__':
    run()
