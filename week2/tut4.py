#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-26 23:35
# @Author : XXX
# @Site : 
# @File : tut4.py
# @Software: PyCharm

'''
    异常处理
    try:
        ...
    except ValueError as e:
        ...
    finally:
        ...

    Raise 抛出异常

    所有的异常类都继承与BaseException
'''

try:
    print('try:')
    a = 100/0
    print('result:',a)
except ValueError as e:
    print('ValueError', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError', e)
    # raise: 把错误上抛到上一层
else:
    print('unknown error!')
finally:
    print('不好意思，出错了！')


# 调用栈


# 如果py单独运行，__name__ == '__main__ 如果py文件被其他模块引入调用的时候就不等于
if __name__ == '__main__':
    '''
        给我们测试调用用的
    '''



