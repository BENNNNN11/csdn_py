#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021-01-21 17:47
# @Author : Jiabin Wang
# @Site : 
# @File : Q1.py
# @Software: PyCharm



class Student(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

# 类变量如果直接用类名引用是全局生效的（即每个对象都会生效）
# self.count是只对当前对象生效

s1 = Student("xiaohong")

s1 = Student("xiaohong")

print(s1.count)