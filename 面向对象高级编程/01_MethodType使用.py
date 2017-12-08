#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 15:40
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 01_MethodType使用.py
# @Software: PyCharm Community Edition

# MethodType：
# 用MethodType将方法绑定到类，并不是将这个方法直接写到类内部，
# 而是在内存中创建一个link指向外部的方法，在创建实例的时候这个link也会被复制。

class Student(object):
    pass

def set_name(self, name):
    self.name = name

s1 = Student()
s2 = Student()
s3 = Student()

#将set_name方法绑定到s1实例上
from types import MethodType

# 给student 创建一个方法 但这里不是在class中创建而是创建了一个链接把外部的set_name 方法用链接指到实例
# MethodType把方法绑定在类实例上时，每个实例有自己单独的指向区域，互不干扰。
s1.set_name = MethodType(set_name, s1)
s2.set_name = MethodType(set_name, s2)
s1.set_name('tony')
s2.set_name('tom')
print(s1.name, ',', s2.name)  # print(s1.name, ',', s2.name)

s3.set_name('tom')  # s3调用方法set_name 报错，没有该方法
# Traceback (most recent call last):
#   File "J:/Python3/Mybook/廖雪峰教程/面向对象高级编程/01_MethodType使用.py", line 31, in <module>
#     s3.set_name('tom')
# AttributeError: 'Student' object has no attribute 'set_name'

# print(s1.name, ',', s2.name)  # print(s1.name, ',', s2.name)
print(s3.name)  # s3调用属性name 报错，同样是没有这个name属性
# Traceback (most recent call last):
#   File "J:/Python3/Mybook/廖雪峰教程/面向对象高级编程/01_MethodType使用.py", line 31, in <module>
#     print(s3.name)
# AttributeError: 'Student' object has no attribute 'name'


#将方法绑定在类上（有None参数）
Student.set_name = MethodType(set_name, Student)
s1 = Student()
s2 = Student()
s3 = Student()
s1.set_name('tony')
s2.set_name('tom')
print(s1.name, ',', s2.name, ',', s3.name)
# tom , tom , tom   三个值都是tom

# 用MethodType将set_name方法绑定到Student类，并不是将这个方法直接写到Student类内部，而是在Student内存中创建一个link指向外部的方法，
# 在创建Student实例的时候这个link也会被复制。
# 所以不管创建多少实例，这些实例和Student类都指向同一个set_name方法。

# s1.set_name('tom')并没有在 s1 这个实例内部创建name属性，而是将name属性创建在外部set_name 方法的内存区中。
# 因为s1 和s2,s3 内部link都指向外部set_name方法的内存区，所以不管s1,s2 还是s3 在调用set_name方法的时候
# 改变的是set_name方法内存区里的name属性，
# 所以s2 调用后会将s1 调用时的赋值覆盖掉 s1 的name值也就改变了，
# 如果新建一个实例s3 在没有调用set_name方法的前提下也会有name属性，
# 因为s3的link指向的set_name方法的内存区，而set_name之前被s1或者s2调用过了。
