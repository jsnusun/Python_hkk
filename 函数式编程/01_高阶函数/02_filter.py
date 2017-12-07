#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 17:57
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 02_filter.py

# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，
# 然后根据返回值是True还是False决定保留还是丢弃该元素。

# 在一个list中，删掉偶数，只保留奇数，可以这么写
def is_even(n):
    return n % 2 == 0


print(list(filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# [2, 4, 6, 8]


def is_odd(n):
    return n % 2 == 1


print(list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
# [1, 3, 5, 7, 9]

# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', ' ', 'C', 'D', None])))
# ['A', 'C', 'D']

# 用filter()这个高阶函数，关键在于正确实现一个“筛选”函数。

# filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


# 用filter求素数
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：
# 首先，列出从2开始的所有自然数，构造一个序列：
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数。