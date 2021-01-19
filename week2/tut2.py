#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020-03-26 01:15
# @Author : XXX
# @Site : 
# @File : tut2.py
# @Software: PyCharm


'''
    设计模式
'''

'''
    列表生成式
'''

d = {'x':'a', 'y':'b', 'z':'c'}
print([k + '=' + v for k,v in d.items()])

# 生成list(1,2,3,...,10)
list(range(1,11))

# 生成list(1*1,2*2,...,10*10)
print([x*x for x in range(1,11)])

# 'abc'  '123'
print([m + n for m in 'abc' for n in '123'])

print([m + n for m in 'a.b.c' for n in '123' if m != '.'])

'''
    生成器
    1. 列表生成
    2. yield
'''

g = (x*x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)

# yield
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a , b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 输出关键词换成yield
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a , b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)

print(next(g))
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)

while True:
    try:
        x = next(g)
        print(x)
    except StopIteration as e:
        print('没有数据了', e.value)
        break


'''
    迭代器
'''

# 判断一个对象是不是可迭代
from collections import Iterable
print(isinstance([], Iterable))

# 判断是不是生成器器对象 Iterator: 既可以用for 循环， 也可以同next()

from collections.abc import Iterator
print(isinstance([], Iterator))


from collections import Iterator
# iter()把可迭代对象转化成生成器
print(isinstance(iter([]), Iterator))



