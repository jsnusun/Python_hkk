#!/usr/bin/python3

# python3基本数据类型示例
# counter = 100      # 整型变量
# miles = 1000.0     # 浮点型变量
# name = "hkkhuang"  # 字符串
#
# print(counter)
# print(miles)
# print(name)

#多个变量赋值
# a, b, c = 1, 2, "huangkeke"
# print(a)
# print(b)
# print(c)

# 标准数据类型
# a, b, c, d = 20, 5.5, True, 4 + 3j
# print(type(a), type(b), type(c), type(d))

# a = 123
# print(isinstance(a, int))


# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# print(isinstance(A(), A))  # returns True
# print(type(A()) == A)      # returns True
# print(isinstance(B(), A))    # returns True
# print(type(B()) == A)        # returns False


# 数值运算
# print(5+4)     # 加法
# print(4.6-4)   # 减法
# print(3*5)     # 乘法
# print(9/3)     # 除法，得到一个浮点数
# print(2//4)    # 除法  得到一个整数
# print(19%3)    # 取余
# print(2**5)    # 乘方

# myStr = 'ILovePython'
#
# print(myStr)  # 输出字符串
# print(myStr[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(myStr[0])  # 输出字符串第一个字符
# print(myStr[2:5])  # 输出从第三个开始到第五个的字符
# print(myStr[2:])  # 输出从第三个开始的后的所有字符
# print(myStr * 2)  # 输出字符串两次
# print(myStr + "TEST")  # 连接字符串

# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
# print('my name is huangkeke')     # 输出字符串
# print("My name is \nhuangkeke")   # 转义字符 \n 表示换行
# print(r"my name is \nhuangkeke")  # 在字符串前面加上r 或者 R 表示原样输出字符串

# 运行结果
# my name is huangkeke
# My name is
# huangkeke
# my name is \nhuangkeke

# 另外，反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
# 注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。

print('Hi,nice to meet you\
my name \
is huangkeke')

print('''Hi,nice to meet you'''
'''my name '''
'''is huangkeke''')