# 面向过程

stu1 = { 'name': 'xiaohong', 'score': 98 }
stu2 = { 'name': 'xiaobai', 'score': 81 }

# 函数
def print_score(stu):
    print('%s: %s' % (stu['name'], stu['score']))


# 面向对象
# 1.设计类
#  属性和方法

class Student(object):
    # 方法  self指向创建的实例本身
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))

# 实例化对象1
xiaohong = Student('xiaohong',98)
print(id(xiaohong))
# 实例化对象2
xiaobai = Student('xiaobai',81)
print(id(xiaobai))
# 实例化对象3
xiaobai = Student('xiaobai',81)
print(id(xiaobai))
# 每次实例化都复制了一个副本并给分配不同的内存空间

# print(xiaobai.name,xiaobai.score)
# print(xiaohong.name,xiaohong.score)

#xiaohong.print_score()
# xiaobai.print_score()

'''
    继承，封装，多态
'''


class Student(object):
    # 方法  self指向创建的实例本身
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name,self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


xiaolv = Student('xiaolv',45)
print(xiaolv.get_grade())


'''
    访问限制
'''
xiaolv.score=90
print(xiaolv.get_grade())


class Student(object):
    # 方法  self指向创建的实例本身
    def __init__(self,name,score):
        self.__name = name   # 私有属性
        self.__score = score  # 私有属性

    def print_score(self):
        print('%s: %s' % (self.__name,self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def set_score(self,score):
        if  0<=score<=100:
            self.__score=score
        else:
            raise ValueError('分数请大于0小于等于100')

    def get_score(self):
        return self.__score

xiaolv = Student('xiaolv',45)


print(xiaolv.set_score(98))
print(xiaolv.get_score())

# python没有真正的是私有，把私有改名称_Student__name
print(xiaolv._Student__name)


'''
    类属性
'''

# 实例属性  必须通过初始化或者实例化对象，通过对象去访问，
class Student(object):
    def __init__(self, name):
        self.name = name
s = Student('Bob')
print(s.name)

# 类属性  不需要实例化对象，直接通过类名访问
class Student(object):
    name = 'Student'

print(Student.name)


