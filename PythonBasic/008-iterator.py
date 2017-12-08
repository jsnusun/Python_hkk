#!/usr/bin/python3
#
# Python3 迭代器与生成器
# 迭代器
#
# 迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
#
# 迭代器是一个可以记住遍历的位置的对象。
#
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
#
# 迭代器有两个基本的方法：iter() 和 next()。
#
# 字符串，列表或元组对象都可用于创建迭代器：

# myList = [1, 2, 3, 4, 5]
# it = iter(myList)
# print(next(it))  #从0开始 读取下一个位置 1
#
# print(next(it))  #从0开始 读取下一个位置 2

# myList = [1, 2, 3, 4, 5]
# it = iter(myList)  #创建迭代器对象
# for x in it:
#     print(x)  #从0开始 读取下一个位置 1
#
# # 执行结果:
# 1
# 2
# 3
# 4
# 5

#
# myList = [1, 2, 3, 4, 5]
# it = iter(myList)  #创建迭代器对象
# for x in it:
#     print(x, end=(" "))  #从0开始 读取下一个位置 1
#
# # 执行结果:
# 1 2 3 4 5


# import sys
# myList = [1, 2, 3, 4, 5]
# it = iter(myList)  #创建迭代器对象
#
# while True:
#     try:
#         print(next(it))
#     except ValueError:
#         print('出现异常')
#
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
# print('----------------')
# for value in d.values():
#     print(value)
#
# print('-----------------')
# for k, v in d.items():
#     print(k, end=':')
#     print(v)
#
# # 执行过程:
# a
# b
# c
# ----------------
# 1
# 2
# 3
# -----------------
# a:1
# b:2
# c:3

# # 字符串循环迭代
# str = 'YZUHKK'
# for s in str:
#     print(s)
#
# # 执行结果:
# Y
# Z
# U
# H
# K
# K
#
# 所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
#
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

# from collections import Iterable
# print(isinstance('1234', Iterable))
# print(isinstance([1,2,3], Iterable))
# print(isinstance(123, Iterable))
#
# # 执行结果
# True
# True
# False

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
#
# for i, value in enumerate(['A','B','YZU']):
#     print(i,value)
#
# # 执行结果:
# 0 A
# 1 B
# 2 YZU

# ==================================列表生成器==================================================
# myList = list(range(1,20))
# print(myList)
#
# # 执行结果:[不包括上限]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

# =======================
# myList = []
# for x in range(1, 11):
#     myList.append(x * x)
#
# print(myList)
#
# # 执行结果:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 但是循环太过于繁琐,使用列表生成器则可以使用一行语句代替循环生成的list
# myList = [x * x for x in range(1, 11)]
# print(myList)
#
# 执行结果:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#
# myList = [x * x for x in range(1, 11) if x % 2 == 0]
# print(myList)
#
# 执行结果:
# [4, 16, 36, 64, 100]
#
# # 还可以使用两层循环，可以生成全排列：
# myList = [m + n for m in 'JSNU' for n in 'YZU']
# print(myList)
#
# # 执行结果
# ['JY', 'JZ', 'JU', 'SY', 'SZ', 'SU', 'NY', 'NZ', 'NU', 'UY', 'UZ', 'UU']

# import os
# myDir = [d for d in os.listdir('.')]
# print(myDir)
#
# # 执行结果:
# ['008-iterator.py', '006-conditionControl.py', '007-loopStructure.py', '005-String.py', '004-python_Number.py', '003_operator.py', '.idea']

# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = []
# for s in L1:
#     if isinstance(s, str):
#         L2.append(s.lower())
#
# print('转换结束')
# print(L2)


# 生成器
# g = (x * x for x in range(10))
# print(g)

# 执行结果:
# <generator object <genexpr> at 0x104a7c888>
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
#
# print(next(g))

# Traceback (most recent call last):
#   File "/Users/hkkhuang/Documents/Python/PythonBasic/008-iterator.py", line 187, in <module>
#     print(next(g))
# StopIteration
# <generator object <genexpr> at 0x103a7c888>
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

#
# g = (x * x for x in range(10))
#
# for x in g:
#     print(x)
#
# # 执行结果
# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81

#
# # 函数实现Fibonacci数列
#
# def fib(mymax):
#     n, a, b = 0, 0, 1
#     while n < mymax:
#         print(b,end=' ')
#         a, b = b, a+b
#         n = n + 1
#     return 'done'
#
# fib(20)
#
# # 执行结果:
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765


# # 函数实现Fibonacci数列
# 函数改为generator 生成器

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1
    return 'done'


f = fib(20)

print(type(f))  # 判断类型为 <class 'generator'>

for x in f:
    print(x, end=' ')

# 执行结果:
# <class 'generator'>
# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 done