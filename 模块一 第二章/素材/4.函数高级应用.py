# 函数的高级应用
# Python中函数即变量


# abs(-10)函数调用，abs是函数本身
print(abs(-10))


f = abs
print(f)
print(f(-10))

# abs函数被覆盖掉
# abs = 10
# abs(-10)

# 代理模式
# 把函数当作参数传递给其他函数
def add(x,y,f):
    return f(x)+f(y)


print(add(-5,6,abs))

# x =-5
# y = 6
# f = abs
# f(x)+f(y) ==> abs(-5) + abs(6)==>11
# return 11

'''
    map函数： 接受两个参数，一个是函数，一个是iterable的可迭代对象
    将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
'''

l = [1,2,3,4,5,6,7,8,9]

def f(x):
    return x*x

m = map(f,l)
print(m)
# print(list(m))

# for n in m:
#     print(n)

print(next(m))
print(next(m))
print(next(m))



# l 列表中每个int转换成字符串
l = [1,2,3,4,5,6,7,8,9]

print(list(map(str,l)))


'''
    reduce函数：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''

l = [4,2,5,7,8,9]  #获得425789

from functools import reduce

def f(x,y):
    return x * 10 + y

print(reduce(f,l))
print(type(reduce(f,l)))


# str()  int()
# '5632'==>5632
# 1. 字符串每个元素取出来，转化成对应的数字,得到一个数字序列
# 2. 通过数字序列每两个*10 相加，得到一个整数

def f(x,y):
    return x * 10 + y

def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
    return digits[s]

s1 = '5632'

nums = reduce(f, map(char2num,s1))

print(type(nums))
print(nums)

'''
    匿名函数：在函数中定义函数，只能在函数内部调用
'''

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def f(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(f, map(char2num,s))

print(str2int('674321'))


# lambda表达式
def str2int(s):
    def char2num(s):
        return DIGITS[s]
    return reduce(lambda x,y:x*10+y,map(char2num,s))
print(str2int('432'))

'''
    装饰器： 在代码运行期间动态增加功能的方式
'''

import datetime


# 装饰器：以一个函数作为参数，并返回一个函数
def log(f):
    def write_log(*args,**kw):
        with open('./a.txt','w') as f1:
            f1.write(f.__name__)
            print('写入日志成功，函数名字是:%s'%f.__name__)
            return f(*args,**kw)
    return write_log

@log
def now():
    print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
# now()


# 调用方式一
# ff = log(now)
#
# ff()
# print(ff.__name__)


# 调用方式二
now()

'''
    Python内置的装饰器 @property @setter
'''

class Student(object):
    def __init__(self,score):
        self.__score = score

    def get_score(self):
         return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value


stu1 = Student(90)

print(stu1.set_score(85))
print(stu1.get_score())


# 加上装饰器，方法变属性
class Student(object):
    def __init__(self,score):
        self.__score = score

    @property
    def score(self):
         return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self.__score = value


stu2 = Student('67')

stu2.score = 59
print(stu2.score)




