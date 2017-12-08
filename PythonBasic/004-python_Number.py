#!/usr/bin/python

#  python 中数字有以下的表示方式：
# 2 进制是以 0b 开头的: 例如: 0b11 则表示十进制的 3
# 8 进制是以 0o 开头的: 例如: 0o11 则表示十进制的 9
# 16 进制是以 0x 开头的: 例如: 0x11 则表示十进制的 17
# a=0b111100
# print(a)
#
# # 分别使用 bin，oct，hex 可输出数字的二进制，八进制，十六进制形式，例如：
# print(bin(a))
# print(oct(a))
# print(hex(a))
#
# 执行结果：
# 60
# 0b111100
# 0o74
# 0x3c


# 数学函数
# 【1】abs(x)  返回数字的绝对值
# print("abs(-40) : ", abs(-40))
# print("abs(100.10) : ", abs(100.10))
#
# # 执行结果
# abs(-40) :  40
# abs(100.10) :  100.1

# # 【2】fabs(x)
# import math   # 导入 math 模块
#
# print ("math.fabs(-45.17) : ", math.fabs(-45.17))
# print ("math.fabs(100.12) : ", math.fabs(100.12))
# print ("math.fabs(100.72) : ", math.fabs(100.72))
# print ("math.fabs(math.pi) : ", math.fabs(math.pi))
#
# # 执行结果
# math.fabs(-45.17) :  45.17
# math.fabs(100.12) :  100.12
# math.fabs(100.72) :  100.72
# math.fabs(math.pi) :  3.141592653589793

# 【3】max(x, y, z,...)  参数可以是序列
# a = [1, 2, 3, 4]
# print(max(a))


