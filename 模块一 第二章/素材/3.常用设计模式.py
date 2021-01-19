# 列表生成式
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k+'='+v for k,v in d.items()])

# 生成list,[1,2,3...10]
print(list(range(1,11)))

# 生成[1*1,2*2,3*3...]
print([x*x for x in range(1,11)])

# 'abc','123' 输出a1,a2,a3,b1,b2,b3
print([m + n for m in 'abc' for n in '123'])

print([m + n for m in 'a.b.c' for n in '123' if m!='.'])

'''
    生成器：
        不必创建完整的list，类似于惰性计算，用来节省内存开支
'''
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)

# yield
# 斐波那契数列 1，1，2，3，5，8
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(6)

# 输出关键字换成yield
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)

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
        print('没有数据了',e.value)
        break


'''
    迭代器： 
'''

# 判断一个对象是否可迭代 Iterable
from collections import Iterable
# print(isinstance([],Iterable))
# print(isinstance({},Iterable))
# print(isinstance('abc',Iterable))
# print(isinstance(123,Iterable))


# 判断一个对象是否是生成器 Iterator
from collections.abc import Iterator
# print(isinstance([],Iterator))
# print(isinstance({},Iterator))
# print(isinstance('abc',Iterator))
# print(isinstance(123,Iterator))


print(isinstance(iter([]),Iterator))
print(isinstance(iter({}),Iterator))
print(isinstance(iter('abc'),Iterator))



