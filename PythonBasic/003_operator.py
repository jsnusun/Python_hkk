#!/usr/bin/python3

# a = 21
# b = 10
# c = 0
#
# c = a + b
# print("1 - c 的值为：", c)
#
# c = a - b
# print("2 - c 的值为：", c)
#
# c = a * b
# print("3 - c 的值为：", c)
#
# c = a / b
# print("4 - c 的值为：", c)
#
# c = a % b
# print("5 - c 的值为：", c)
#
# # 修改变量 a 、b 、c
# a = 2
# b = 3
# c = a ** b
# print("6 - c 的值为：", c)
#
# a = 10
# b = 5
# c = a // b
# print("7 - c 的值为：", c)

# 执行结果
# 1 - c 的值为： 31
# 2 - c 的值为： 11
# 3 - c 的值为： 210
# 4 - c 的值为： 2.1
# 5 - c 的值为： 1
# 6 - c 的值为： 8
# 7 - c 的值为： 2

# python比较运算符
# a = 1
# b = 2
# c = 0
#
# if (a == b):
#     print("1 - a 等于 b")
# else:
#     print("1 - a 不等于 b")
#
# if (a != b):
#     print("2 - a 不等于 b")
# else:
#     print("2 - a 等于 b")
#
# if (a < b):
#     print("3 - a 小于 b")
# else:
#     print("3 - a 大于等于 b")
#
# if (a > b):
#     print("4 - a 大于 b")
# else:
#     print("4 - a 小于等于 b")
#
# # 修改变量 a 和 b 的值
# a = 10;
# b = 20;
# if (a <= b):
#     print("5 - a 小于等于 b")
# else:
#     print("5 - a 大于  b")
#
# if (b >= a):
#     print("6 - b 大于等于 a")
# else:
#     print("6 - b 小于 a")

# 运行结果
# 1 - a 不等于 b
# 2 - a 不等于 b
# 3 - a 小于 b
# 4 - a 小于等于 b
# 5 - a 小于等于 b
# 6 - b 大于等于 a

#
# # Python赋值运算符
# a = 21
# b = 10
# c = 0
#
# c = a + b
# print("1 - c 的值为：", c)
#
# c += a
# print("2 - c 的值为：", c)
#
# c *= a
# print("3 - c 的值为：", c)
#
# c /= a
# print("4 - c 的值为：", c)
#
# c = 2
# c %= a
# print("5 - c 的值为：", c)
#
# c **= a
# print("6 - c 的值为：", c)
#
# c //= a
# print("7 - c 的值为：", c)
#
# # 执行结果：
# 1 - c 的值为： 31
# 2 - c 的值为： 52
# 3 - c 的值为： 1092
# 4 - c 的值为： 52.0
# 5 - c 的值为： 2
# 6 - c 的值为： 2097152
# 7 - c 的值为： 99864

# Python 位运算符
# a = 60  # 60 = 0011 1100
# b = 13  # 13 = 0000 1101
# c = 0
#
# c = a & b;  # 12 = 0000 1100
# print("1 - c 的值为：", c)
#
# c = a | b;  # 61 = 0011 1101
# print("2 - c 的值为：", c)
#
# c = a ^ b;  # 49 = 0011 0001
# print("3 - c 的值为：", c)
#
# c = ~a;  # -61 = 1100 0011
# print("4 - c 的值为：", c)
#
# c = a << 2;  # 240 = 1111 0000
# print("5 - c 的值为：", c)
#
# c = a >> 2;  # 15 = 0000 1111
# print("6 - c 的值为：", c)

# 执行结果
# 1 - c 的值为： 12
# 2 - c 的值为： 61
# 3 - c 的值为： 49
# 4 - c 的值为： -61
# 5 - c 的值为： 240
# 6 - c 的值为： 15

# Python逻辑运算符
# a = 10
# b = 20
#
# if (a and b):
#     print("1 - 变量 a 和 b 都为 true")
# else:
#     print("1 - 变量 a 和 b 有一个不为 true")
#
# if (a or b):
#     print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#     print("2 - 变量 a 和 b 都不为 true")
#
# # 修改变量 a 的值
# a = 0
# if (a and b):
#     print("3 - 变量 a 和 b 都为 true")
# else:
#     print("3 - 变量 a 和 b 有一个不为 true")
#
# if (a or b):
#     print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#     print("4 - 变量 a 和 b 都不为 true")
#
# if not (a and b):
#     print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
# else:
#     print("5 - 变量 a 和 b 都为 true")

# 执行结果
# 1 - 变量 a 和 b 都为 true
# 2 - 变量 a 和 b 都为 true，或其中一个变量为 true
# 3 - 变量 a 和 b 有一个不为 true
# 4 - 变量 a 和 b 都为 true，或其中一个变量为 true
# 5 - 变量 a 和 b 都为 false，或其中一个变量为 false


# python 成员运算符

# a = 10
# b = 20
# myList = [1, 2, 3, 4, 5];
#
# if (a in myList):
#     print("1 - 变量 a 在给定的列表中 list 中")
# else:
#     print("1 - 变量 a 不在给定的列表中 list 中")
#
# if (b not in myList):
#     print("2 - 变量 b 不在给定的列表中 list 中")
# else:
#     print("2 - 变量 b 在给定的列表中 list 中")
#
# # 修改变量 a 的值
# a = 2
# if (a in myList):
#     print("3 - 变量 a 在给定的列表中 list 中")
# else:
#     print("3 - 变量 a 不在给定的列表中 list 中")
#
# # 执行结果
# 1 - 变量 a 不在给定的列表中 list 中
# 2 - 变量 b 不在给定的列表中 list 中
# 3 - 变量 a 在给定的列表中 list 中

# python身份运算符
# a = 20
# b = 20
#
# if (a is b):
#     print("1 - a 和 b 有相同的标识")
# else:
#     print("1 - a 和 b 没有相同的标识")
#
# if (id(a) == id(b)):
#     print("2 - a 和 b 有相同的标识")
# else:
#     print("2 - a 和 b 没有相同的标识")
#
# # 修改变量 b 的值
# b = 30
# if (a is b):
#     print("3 - a 和 b 有相同的标识")
# else:
#     print("3 - a 和 b 没有相同的标识")
#
# if (a is not b):
#     print("4 - a 和 b 没有相同的标识")
# else:
#     print("4 - a 和 b 有相同的标识")

# 执行结果：
# 1 - a 和 b 有相同的标识
# 2 - a 和 b 有相同的标识
# 3 - a 和 b 没有相同的标识
# 4 - a 和 b 没有相同的标识

# a = [1, 2, 3]
# b = a
# print(b)
# print(b is a)
# print(b == a)
# b = a[:]
# print(b)
# print(b is a)
# print(b == a)
# # 执行结果
# [1, 2, 3]
# True
# True
# [1, 2, 3]
# False
# True


# # 运算符优先级
# a = 20
# b = 10
# c = 15
# d = 5
# e = 0
#
# e = (a + b) * c / d  # ( 30 * 15 ) / 5
# print("(a + b) * c / d 运算结果为：", e)
#
# e = ((a + b) * c) / d  # (30 * 15 ) / 5
# print("((a + b) * c) / d 运算结果为：", e)
#
# e = (a + b) * (c / d);  # (30) * (15/5)
# print("(a + b) * (c / d) 运算结果为：", e)
#
# e = a + (b * c) / d;  # 20 + (150/5)
# print("a + (b * c) / d 运算结果为：", e)
#
# 执行结果：
# (a + b) * c / d 运算结果为： 90.0
# ((a + b) * c) / d 运算结果为： 90.0
# (a + b) * (c / d) 运算结果为： 90.0
# a + (b * c) / d 运算结果为： 50.0