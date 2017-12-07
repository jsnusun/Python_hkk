#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 18:31
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 02_返回函数.py

# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 实现一个可变参数的求和。
# 通常情况下，求和的函数是这样定义的：
def clac_sum(*args):
    my_sum = 0
    for n in args:
        my_sum = my_sum + n
    return my_sum

# 如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？
# 可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def clac_sum():
        my_sum = 0
        for n in args:
            my_sum = my_sum + n
        return my_sum
    return clac_sum

f = lazy_sum(1, 3, 5, 7, 9)
print(f)  # <function lazy_sum.<locals>.clac_sum at 0x0124BB70>
# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：

# 调用函数f时，才真正计算求和的结果
print(f())  # 25

# 在这个例子中，我们在函数lazy_sum中又定义了函数clac_sum，
# 并且内部函数clac_sum 可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数clac_sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。

# 注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print(f1 == f2)  # False

# f1()和f2()的调用结果互不影响。



# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，
# 其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

# 需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
