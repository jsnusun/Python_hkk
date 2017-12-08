#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 9:30
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : StringIO和BytesIO.py

# StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
# StringIO顾名思义就是在内存中读写str。
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

# from io import StringIO
# f = StringIO()
# a = f.write('hello')
# print(a)
# b = f.write(' ')
# print(b)
# c = f.write('world!')
# print(c)
# # 5
# # 1
# # 6
# # write() 返回写入字符数
#
# print(f.getvalue())  # hello world!
# # getvalue()方法用于获得写入后的str。
#
# # 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
# from io import StringIO
# f = StringIO('Hello!\nWorld!\nHi!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())
#
# # Hello!
# # World!
# # Hi!
#
# from io import StringIO
# f = StringIO('Hello!\nWorld!\nHi!')
# while True:
#     s = f.read()
#     if s == '':
#         break
#     print(s.strip())
#
# # Hello!
# World!
# Hi!


# BytesIO
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，
# 创建一个BytesIO，然后写入一些bytes

# from io import BytesIO
# f = BytesIO()
# a = f.write('中文字符'.encode('utf-8'))
# print(a)
# print(f.getvalue())
# 12
# b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6'
# 写入的不是str，而是经过UTF-8编码的bytes


from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6')
print(f.read())
f.seek(0)  # 回到文件头
print(f.read().decode('utf-8'))
print(f.getvalue())
print(f.getvalue().decode('utf-8'))

# b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6'
#
# b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6'
# 中文字符

# b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6'
# 中文字符
# b'\xe4\xb8\xad\xe6\x96\x87\xe5\xad\x97\xe7\xac\xa6'
# 中文字符
