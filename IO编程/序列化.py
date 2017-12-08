#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 14:38
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 序列化.py

import pickle

# 程序在运行过程中,所有的变量都是在内存中
# 比如,定义一个dict
# d = dict(name='Bob', age=20, score=90)

# 可以随时的修改变量,比如将name修为Tom,但是在程序结束,变量所占用的内存被系统全部收回,
# 如果没有把修改的Tom存储到磁盘,下次启动程序,变量又被初始化为Bob

# 把变量从内存中变成可存储或者传输的过程称为 序列化  Python中序列化叫 pickling
# 在完成序列化之后，就可以把序列化之后的内容写入磁盘，或者通过网络传输到别的机器

# 反过来，把变量从序列化的对象重新读取到内存中称为反序列化  unpickling
# 在Python中 提供了pickle模块来实现序列化
# 首先，将一个对象序列化并写入文件


# import pickle
# d = dict(name='Bob', age=20, score=90)
# pickle_bytes = pickle.dumps(d)
#
# # <class 'bytes'>
# print(type(pickle_bytes))  # pickle.dumps()方法将任意对象序列化成一个bytes, 然后可以将这个bytes 写入文件

# print(pickle_bytes)
# b'\x80\x03}q\x00(X\x05\x00\x00\x00scoreq\x01KZX\x04\x00\x00\x00nameq\x02X\x03\x00\x00\x00Bobq\x03X\x03\x00\x00\x00ageq\x04K\x14u.'

# 另一个方法是pickle.dump()  直接将一个对象序列化成一个file_like Object

# with open('dump.txt', 'wb') as fileWriter:
#     pickle.dump(d, fileWriter)

# 看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。


# 当我们要把对象从磁盘读取到内存时候，可以先将内容读取到一个bytes, 然后用 pickle.loads()方法反序列化出对象
# 也可以直接使用pickle.load() 方法从一个file-like Object中直接反序列化出对象

# with open('dump.txt', 'rb') as fileReader:
#     d = pickle.load(fileReader)
#
# print(d)  # {'score': 90, 'name': 'Bob', 'age': 20}
# 变量的内容又回来了！当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，
# 并且可能不同版本的Python彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。

# JSON
# 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，
# 比如XML，但更好的方法是序列化为JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，
# 也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。

# JSON表示的对象就是标准的JavaScript语言的对象，

# JSON和Python内置的数据类型对应如下：
# JSON类型 	    Python类型
#  {} 	         dict
#  [] 	         list
# "string" 	     str
# 1234.56 	     int或float
# true/false 	 True/False
# null      	 None

# Python 内置的json模块提供了非常完善的Python对象到JSON格式的转换

import json
d = dict(name='Bob', age=20, score=90)
json_value = json.dumps(d)
print(type(json_value))   # <class 'str'>
print(json_value)   # {"score": 90, "age": 20, "name": "Bob"}

with open('json.txt', 'w') as file_object:
    file_object.write(json_value)  # 写入的是文本


# dumps()方法返回一个str，内容就是标准的JSON。
# 类似的，dump()方法可以直接把JSON写入一个file-like Object
with open('json.txt', 'w') as file_object:
    json.dump(d, file_object)  # 写入的是文本

# 反序列化
with open('json.txt', 'r') as file_object:
    json_bytes = file_object.read()
    json_str = json.loads(json_bytes)
    print(json_str)

with open('json.txt', 'r') as file_object:
    json_str = json.load(file_object)
    print(json_str)

