#!/usr/bin/python3

# 1------------------------------------
# 递归
# 函数的调用可以再一个函数中调用另一个函数,其中一个函数自己内部调用自己就是函数的递归调用
# 满足递归调用的一个条件是  必须有区域结束的条件


# def recursion(num):
#     if num == 1:
#         return 1
#     return num * recursion(num-1)
#
#
# print('10! =', recursion(10))


# 2------------------------------------
# 切片
# 取一个list或者tuple中的部分元素
# List1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#
# # 取前三个元素
# print(List1[0], List1[1], List1[2])
# # 执行结果:
# # A B C
#
# # 取出前5个元素
# result = []
# n = 5
# for i in range(n):
#     result.append(List1[i])
#
# print(result)
#
# # 执行结果:
# # ['A', 'B', 'C', 'D', 'E']
#
# for i in result:
#     print(i, end=' ')
# # 执行结果:
# # A B C D E


# Python中提供了切片的操作符
# List1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
#
# print(List1[0:5])
#
# # 执行结果:
# # ['A', 'B', 'C', 'D', 'E']
#
# print(List1[:5])  # 索引从0 开始可以省略
# # 执行结果:
# # ['A', 'B', 'C', 'D', 'E']
#
#
# # 截取中间部分
# print(List1[3:6])
#
# # 执行结果:
# # ['D', 'E', 'F']
#
#
# # 既然支持倒数索引,同样支持倒数切片
# print(List1[-3:])
# # 执行结果:
# # ['E', 'F', 'G']
#
#
# print(List1[-3:-2])
# # 执行结果:
# # ['E']

# 倒数第一个的索引是-1


# List2 = list(range(100))
#
# # 取出前十个数
# print(List2[0:10])
# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# # 取出后十个数
# print(List2[-10:])
# # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
#
#
# # 取出11-20个说
# print(List2[10:20])
# # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
#
#
# # 步长为2取出前十个数
# print(List2[0:10:2])
# # [0, 2, 4, 6, 8]
#
#
# # 所有数,步长为5,取出
# print(List2[::5])
# # [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
#
#
# # 什么都不写,   [:]  表示 原样赋值一个list
# print(List2[:])
# # [0, 1, 2, 3, 4, ...., 95, 96, 97, 98, 99]


# tuple也是一种list,不过tuple不可以改变,但是可以切片
# Tuple1 = tuple(range(10))
#
# print(Tuple1[:])
# # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)


# 3高阶函数------------------------------------
# higher-order function
# 变量可以指向函数
# print(abs(-8))  # 结果为8
#
# print(abs)  #<built-in function abs>

# 调用函数后,可以将结果赋值给变量
# x = abs(-6)
# print(x)

# 函数本身可以赋值给变量,也就是变量指向函数
# fun = abs
# print(fun)  # 此时的变量fun <built-in function abs>
#
# 变量fun已经指向abs函数本身,直接调用abs()函数和调用变量fun()是一样的
# print(fun(-8))  # 8

# 其实函数名也是变量,将abs函数指向一个整形对象
# abs = 8

# abs(-8)
# Traceback (most recent call last):
#   File "/Users/hkkhuang/Documents/Python/PythonBasic/011-LXF-AdvancedFeatures.py", line 136, in <module>
#     abs(-8)
# TypeError: 'int' object is not callable


# print(abs)  # 8


# 传入函数------------------------------------
# def my_add(x, y, fun):
#     return fun(x) + fun(y)

# 执行过程:
# x = 2
# y = -6
# fun = abs
# fun(x) + fun(y) => abs(x) +abs(y) => 2+6=8

# print(my_add(2, -6, abs))  # 8



# map()/reduce()------------------------------------
# python内建函数

# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
# f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下:


# def f(x):
#     return x*x
#
#
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list_result = map(f, list1)
# print(list(list_result))

# print(list_result)  #<map object at 0x103371ac8>

# 执行结果:
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# ---------------------
# def f(x):
#     return x*x
#
#
# L = []
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for x in list1:
#     L.append(f(x))
#
# print(L)
# #
# # 执行结果:
# # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# ------------------------------------
# map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(str, list1)))

# 执行结果:
# ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']


# reduce()函数------------------------------------
# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# from functools import reduce
#
#
# def f(x, y):
#     return x*10 +y
#
#
# # 把序列[1, 2, 3, 4, 5] 转换成整数12345
# print(reduce(f, [1, 2, 3, 4, 5]))  # 12345


# 将字符串转换成int------------------------------------
from functools import reduce


def fun(x, y):
    return x*10 +y


def CHAR_TO_NUM(s):
    return{'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


# print(list(map(char_to_num, '12345')))  # [1, 2, 3, 4, 5]

print(reduce(fun, list(map(CHAR_TO_NUM, '12345'))))  # 12345



# ------------------------------------

from functools import reduce

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))




# ------------------------------------
CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))




# 1------------------------------------

# 1------------------------------------

# 1------------------------------------

# 1------------------------------------
