#!/usr/bin/python3

# class MyClass:
#     """一个简单的类实例"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
#
#
# # 实例化类
# x = MyClass()
#
# # 访问类的属性和方法
# print("MyClass 类的属性 i 为：", x.i)
# print("MyClass 类的方法 f 输出为：", x.f())

# 执行结果:
# MyClass 类的属性 i 为： 12345
# MyClass 类的方法 f 输出为： hello world


# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#
# def print_score(stu):
#     print('姓名:%s,分数:%d' % (stu.name, stu.score))
#
# stu = Student('zhangsan', 99)
# print_score(stu)
# #
# # 执行结果:
# # 姓名:zhangsan,分数:99

# class Student(object):
#
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
#
#     def print_score(self):
#         print('姓名:%s,分数:%d' % (self.name, self.score))
#
# stu = Student('zhangsan', 99)
# stu.print_score()
# #
# # 执行结果:
# # 姓名:zhangsan,分数:99
#
# class Student(object):
#
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('姓名:%s,分数:%d' % (self.__name, self.__score))
#
#
# # stu = Student('zhangsan', 99)
# # stu.print_score()
# # # 执行结果:
# # # 姓名:zhangsan,分数:99
#
# stu = Student('zhangsan', 99)
# print('姓名:%s,分数:%d' % (stu.name, stu.score))
# # 执行结果:
# # Traceback (most recent call last):
# #   File "/Users/hkkhuang/Documents/Python/PythonBasic/ClassTest.py", line 67, in <module>
# #     print('姓名:%s,分数:%d' % (stu.name, stu.score))
# # AttributeError: 'Student' object has no attribute 'name'



# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('姓名:%s,分数:%d' % (self.__name, self.__score))
#
#     def set_name(self, name):
#         self.__name = name;
#
#     def set_score(self, score):
#         self.__score = score
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#
# stu = Student('zhangsan', 99)
# print('姓名:%s,分数:%d' % (stu.get_name(), stu.get_score()))
#
# stu.set_name('zhangsnasan')
# stu.set_score(90)
#
# print('姓名:%s,分数:%d' % (stu.get_name(), stu.get_score()))
# # 执行结果:
# # 姓名:zhangsan,分数:99
# # 姓名:zhangsnasan,分数:90


#
#
# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
#
# dog = Dog()
# cat = Cat()
#
# dog.run()
# cat.run()
#
# # 执行结果:
# # Animal is running...
# # Animal is running...




class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


class Cat(Animal):
    def run(self):
        print('Cat is running...')

    def speak(self):
        print('Cat speak miao miao...')


dog = Dog()
cat = Cat()

dog.run()
cat.run()

# 执行结果:
# Dog is running...
# Cat is running...

class Timer(object):
    def run(self):
        print('Start...')