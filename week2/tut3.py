#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-26 01:39
# @Author : XXX
# @Site : 
# @File : tut3.py
# @Software: PyCharm

'''
    python中的内置高级函数
'''
print(abs(-10))
# abs(-10)函数调用
# abs函数声明

f = abs
print(f(-10))

# 把函数当参数传递给其他函数
# 代理模式


def add(x,y,f):
    return f(x) + f(y)


print(add(-5, 6, abs))


'''
    map()
'''
l = [1,2,3,4,5,6,7,8,9]
def f(x):
    return x*x

m = map(f,l)
print(m)
# print(list(m))
for n in m:
    print(n)

# l 列表中每个int转换成字符串
l = [1,2,3,4,5,6,7,8,9]
print(list(map(str, l)))



'''
    reduce函数：
'''
from functools import reduce
l = [4,2,5,6,7,7] # 获得425677
def f(x, y):
    return x * 10 + y
print(reduce(f, l))


'''
    str(), int()
'''
# '3245' -> 3245
# 1. 字符串每个元素取出来，转化成相应的数字，得到一个数字序列
# 2. 乘10相加
def f(x, y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1,'2': 2,'3': 3,'4': 4,'5': 5,'6': 6,'7': 7,'8': 8,'9': 9}
    return digits[s]
s1 = '123423'
n = reduce(f, map(char2num,s1))
print(n)

'''
    匿名函数：在函数中定义函数，内部函数，之内内部调用
'''
DIG = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def f(x, y):
        return x * 10 + y
    def char2num(s):
        return DIG[s]
    return reduce(f, map(char2num,s))

print(str2int('1324234'))

# lambda 表达式
def str2int(s):
    def char2num(s):
        return DIG[s]
    return reduce(lambda x,y: x*10+y, map(char2num,s))

print(str2int('234'))


'''
    装饰器模式： 在代码运行期间动态增加功能
    @property 
    @setter
'''
import datetime

# 装饰器： 以一个函数作为参数， 返回一个函数

def log(f):
    def write_log(*args, **kwargs):
        with open('./a.txt', 'w') as f1:
            f1.write(f.__name__)
            print('写入日志成功，函数名字是：%s' %f.__name__)
            return f(*args, **kwargs)
    return write_log
@log
def now():
    print(datetime.datetime.now().strftime('%Y-%M-%D %H:%M:%S'))

now()


# ff = log(now)
# now()


'''
    内置的装饰器：
'''

class Student(object):
    def __init__(self, score):
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')

        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self.__score = value

stu1 = Student(90)
print(stu1.set_score(85))
print(stu1.get_score())


# 加上装饰器，方法变属性
class Student(object):
    def __init__(self, score):
        self.__score = score

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')

        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self.__score = value

stu2 = Student(67)
stu2.score = 59
print(stu2.score)
