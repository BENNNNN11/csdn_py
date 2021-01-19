class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    pass

class Cat(Animal):
    pass

dog = Dog()
# dog.run()

cat = Cat()
# cat.run()

class Dog(Animal):
    def run(self): # 重写
        # 调用父类的run方法
        # super().run()
        print('Dog is running')

    def eat(self):
        print('eat meat')


dog = Dog()
dog.run()


class Cat(Animal):
    def run(self): # 重写
        # 调用父类的run方法
        # super().run()
        print('Cat is running')

    def eat(self):
        print('eat fish')


'''
    多态
'''

b=Animal() # b是Animal类型
c=Dog() # c是Dog类型


print(isinstance(b,Animal))
print(isinstance(c,Dog))
print(isinstance(c,Animal))
print(isinstance(b,Dog))

# 调用run_twice方法，需要传递Animal类的对象或者Animal的子类
def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Dog())
run_twice(Cat())

run_twice(Animal())

'''
    类型判断
'''

import types
def fn():
    pass

print(type(fn)==types.FunctionType)

print(type(abs)==types.BuiltinFunctionType)


# getattr(),setattr(),hasattr()

class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

# obj 有属性'x'吗？
print(hasattr(obj,'x'))
print(obj.x)



# 动态设置一个属性'y'
setattr(obj,'y',19)
print(hasattr(obj,'y'))
print(getattr(obj,'y'))


# dir()
print(obj.__dir__())
print(dir(obj))

a = [1,2]
print(len(a))
print(a.__len__())



