#!/usr/bin/python3
# 递归
# 函数的调用可以再一个函数中调用另一个函数,其中一个函数自己内部调用自己就是函数的递归调用
# 满足递归调用的一个条件是  必须有区域结束的条件


def recursion(num):
    if num == 1:
        return 1
    return num * recursion(num-1)


print('10! =', recursion(10))
