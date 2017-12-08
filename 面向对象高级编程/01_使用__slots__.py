#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 15:33
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 01_使用__slots__.py
# @Software: PyCharm Community Edition

# # 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，
# # 这就是动态语言的灵活性。
#
# # 先定义class：
#
class Student(object):
    pass

#
# # 给实例绑定一个属性：
# s = Student()
# s.name = 'zhangsan'  # 动态给实例绑定一个属性
# print(s.name)
# # zhangsan
#
#
# # 可以尝试给实例绑定一个方法：
# def set_age(self, age):
#     self.age = age
#
# from types import MethodType
# s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
# s.set_age(25)  # 调用实例方法
# print(s.age)  # 测试结果
# # 执行结果
# 25

from types import MethodType
# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


# Student.set_score = set_score   # 给class绑定方法
Student.set_score = MethodType(set_score, Student)   # 给class绑定方法

s1 = Student()
s1.set_score(100)
print(s1.score)
# 执行结果
100

# 通常情况下，上面的set_score方法可以直接定义在class中，
# 但动态绑定允许我们在程序运行的过程中动态给class加上功能
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


s2 = Student()
s2.name = 'Tom'   # 绑定属性'name'
s2.age = 24   # 绑定属性'age'
s2.score = 99   # 绑定属性'score'
# Traceback (most recent call last):
#   File "J:/Python3/Mybook/廖雪峰教程/面向对象高级编程/01_使用__slots__.py", line 64, in <module>
#     s2.score = 99   # 绑定属性'score'
# AttributeError: 'Student' object has no attribute 'score'

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的

class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.score = 99
print(g.score)
# 执行结果
# 99