#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/7 20:35
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : BinaryFileRW.py
"""
二进制文件的读写操作
"""

import struct
filename = "binary.data"
# 写入文件
with open(filename, 'wb') as file_write:
    byte_i = struct.pack('i', 1000)  # 'i' 表示对int类型进行打包
    file_write.write(byte_i)

    byte_f = struct.pack('f', 1000.23)  # 'f' 表示对float类型进行打包
    file_write.write(byte_f)

    byte_d = struct.pack('d', 1000.456)  # 'd' 表示对double类型进行打包
    file_write.write(byte_d)

# 读取文件
with open(filename, 'rb') as file_reader:
    byte_len = 4
    byte_i = file_reader.read(byte_len)  # 读取int类型的4个字节的二进制数据
    print(struct.unpack('i', byte_i))  # 解压为原来int数据

    byte_f = file_reader.read(byte_len)  # 读取float类型的4个字节的二进制数据
    print(struct.unpack('f', byte_f))  # 解压为原来float数据

    byte_len = 8
    byte_d = file_reader.read(byte_len)  # 读取double类型的8个字节的二进制数据
    print(struct.unpack('d', byte_d))  # 解压为原来double数据

# 使用到struct进行打包成二进制字符串或者相应的解包成元组
#
# 注意: unpack返回的是tuple
# (1000,)
# (1000.22998046875,)
# (1000.456,)


