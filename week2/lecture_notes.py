#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-25 23:48
# @Author : XXX
# @Site : 
# @File : lecture_notes.py
# @Software: PyCharm

'''
    面向对象三大特征：
        继承，封装，多态
'''

class Students():
    # __init__相当于构造函数，self是指类自己本身
    # 传入两个行参
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

# 实例化对象
xiaobai = Students('xiaobai', 45)


print(xiaobai.get_grade())


'''
    访问限制
'''

class Students(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def set_score(self, score):
        self.__score = score

    def get_score(self):
        return self.__score


xiaolv = Students('xiaolv', 45)
xiaolv.set_score(80)
print(xiaolv.get_score())


# python是没有真正的私有，把私有改名成了_Student__name

'''
    类属性： 不需要实例化，直接通过类名访问
    实例属性：必须通过初始化或实例化对象，通过对象访问
'''

class Student(object):
    name = 'Student'
print(Student.name)