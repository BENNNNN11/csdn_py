#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-22 22:58
# @Author : XXX
# @Site : 
# @File : week1_tut.py
# @Software: PyCharm

# def func(*parameter): 可变参数的函数
def my_sum(*numbers):
    result = 0
    for item in numbers:
        result += item
    return result

print(my_sum(5,6,7,8,))

# 传入list
nums = [1,2,3]
print(my_sum(*nums))
# 默认参数
# 可变参数
# 关键字参数: 字典形式，可选项
def students(name, age, **kw):
    if 'city' in kw:
        pass
    print("name: ", name, "age: ", age, "others: ", kw)


students("yh", 18, gender='male', nation='China')

# 或者通过字典传入
dicts = {'city': 'Beijing', 'gender': 'female'}
students('mike', 78, **dicts)


def f1(a, b, c=0, *args, **kw):
    pass


def f2(a, b, c=0, *, d, **kw):
    # 可选参数只接受名为d的参数
    pass

################## 文件读写 ######################

#