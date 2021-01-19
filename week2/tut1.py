#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-26 00:51
# @Author : XXX
# @Site : 
# @File : tut1.py
# @Software: PyCharm

'''
    继承
'''

class Animal(object):

    def run(self):
        print('Animal is running')

class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
dog.run()



class Dog(Animal):
    def run(self): # 重写
        # 调用父类的方法
        # super().run()
        print('dog is running')
    def eat(self):
        print('eat meat')

dog = Dog()
dog.run()

'''
    多态： 代码运行时才确定对象的具体类型
'''
b = Animal()
c = Dog()

print(isinstance(b, Animal))
print(isinstance(c, Animal))

def run_twice(animal):
    animal.run()
    animal.run()
