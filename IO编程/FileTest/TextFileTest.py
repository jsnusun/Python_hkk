#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 20:48
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : TextFileTest.py

# 打开文件关闭文件操作
"""
使用open()方法代开文件后一定要保证文件可以正常关闭
所以我们对文件的操作使用try 应对可能会出现的异常
在finally中将文件关闭，这样能够保证在正常或者出现一场的情况下都能正常将文件关闭

注：不能把open语句放在try块里，因为当打开文件出现异常时，文件对象file_object无法执行close()方法。
"""

# 解决 写入中文到文件乱码  在打开文件时候指定编码方式
# file_object01 = open('test01.txt', 'w')  会出现乱码  需要指定编码方式
# file_object01 = open('test01.txt', 'w', encoding='gbk')
file_object01 = open('test01.txt', 'w', encoding='utf-8')
try:
    all_the_text = file_object01.write('这是文本文件的读写操作')
finally:
    file_object01.close()

# 使用with 操作文件，这样Python会在我们不需要使用文件的时候自动将文件关闭
# with open('test01.txt', 'r') as file_object02:  # 不制定编码方式会出现错误

# with open('test01.txt', 'r', encoding='gbk') as file_object02:  # 写入和读取的编码要一致
with open('test01.txt', 'r', encoding='utf-8') as file_object02:
    all_the_text = file_object02.read()
    print(all_the_text)

#  在文件写入时候指定了编码方式，那么在读取时候也要制定编码方式 否则会出现错误
# Traceback (most recent call last):
#   File "J:/Python3/Mybook/廖雪峰教程/IO编程/FileTest/TextFileTest.py", line 25, in <module>
#     all_the_text = file_object02.read()
# UnicodeDecodeError: 'gbk' codec can't decode byte 0xaf in position 22: illegal multibyte sequence