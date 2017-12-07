#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 16:37
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 01_map_reduce.py

# Python内建了map()和reduce()函数。
# map()函数接收两个参数，一个是函数，一个是Iterable，
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 举例说明，比如我们有一个函数f(x)=x2，
# 要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：


def f(x):
    return x * x


result = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(type(result))   # <class 'map'>
print(list(result))   # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，
# 因此通过list()函数让它把整个序列都计算出来并返回一个list。


# map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，
# 比如，把这个list所有数字转为字符串：

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# 执行结果
# ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
# 这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 即：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

from functools import reduce


def add(x, y):
    """reduce()练习，实现累加"""
    return x + y


r = reduce(add, [1, 2, 3, 4, 5, 6])
print(type(r))  # <class 'int'>
print(r)  # 21

from functools import reduce


def factorial(x, y):
    """
    reduce()练习，实现阶乘
    """
    return x * y


r = reduce(factorial, [1, 2, 3, 4, 5])
print(r)  # 120


from functools import reduce


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,  '9': 9}[s]

    # print(list(map(char2num, s)))  # [1, 2, 3, 4, 5]
    return reduce(fn, map(char2num, s))

# 考虑到字符串str也是一个序列
print(str2int('12345'))  # 12345


from functools import reduce


# 考虑到字符串str也是一个序列
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,  '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('12345'))  # 12345


# 练习
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
def normalize(name):
    return name[0].upper() + name[1:].lower()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：
# print(sum([1, 2, 3, 4, 5]))

from functools import reduce


def prod(L):
    def fn(x, y):
        return x *y

    return reduce(fn, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 3 * 5 * 7 * 9 = 945
# 测试成功!