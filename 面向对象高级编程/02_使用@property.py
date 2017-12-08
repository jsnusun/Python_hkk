#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 16:13
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 02_使用@property.py
# @Software: PyCharm Community Edition

# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# class Student(object):
#     pass
#
#
# s = Student()
# s.score = 9999
# print(s.score)  # 执行结果 9999


# 这显然不合逻辑，为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

# class Student(object):
#     """
#     Student类
#     用于练习使用@property
#     """
#     # def __init__(self, score):
#     #     self._score = score
#
#     def set_score(self, value):
#         if not isinstance(value, int):
#             raise ValueError('score must be an integer!')
#         if value < 0 or value > 100:
#             raise ValueError('score must between 0 ~ 100!')
#         self._score = value
#
#     def get_score(self):
#         return self._score
#
# s = Student()
# s.set_score(100)
# print(s.get_score())

# s.set_score('abc')
# print(s.get_score())
# Traceback (most recent call last):
#   File "J:/Python3/Mybook/廖雪峰教程/面向对象高级编程/02_使用@property.py", line 44, in <module>
#     s.set_score('abc')
#   File "J:/Python3/Mybook/廖雪峰教程/面向对象高级编程/02_使用@property.py", line 32, in set_score
#     raise ValueError('score must be an integer!')
# ValueError: score must be an integer!

# s.set_score(999)
# print(s.get_score())
# Traceback (most recent call last):
#   File "J:/Python3/Mybook/廖雪峰教程/面向对象高级编程/02_使用@property.py", line 53, in <module>
#     s.set_score(999)
#   File "J:/Python3/Mybook/廖雪峰教程/面向对象高级编程/02_使用@property.py", line 34, in set_score
#     raise ValueError('score must between 0 ~ 100!')
# ValueError: score must between 0 ~ 100!

# 上面的调用方法又略显复杂，没有直接用属性这么直接简单。
# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
# 装饰器（decorator）可以给函数动态加上功能
# 对于类的方法，装饰器一样起作用, Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):
    # @property的实现比较复杂
    # 把一个getter方法变成属性，只需要加上 @ property就可以了，
    # 此时，@property本身又创建了另一个装饰器 @score.setter
    # 负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value