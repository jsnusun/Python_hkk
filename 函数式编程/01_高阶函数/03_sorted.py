
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 18:19
# @Author  : huangkeke
# @Email   : hkkhuang@163.com
# @File    : 03_sorted.py

# 排序算法
# 排序也是在程序中经常用到的算法。
# 无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。
# 如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？
# 直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

print(sorted([36, 5, -12, 9, -21]))
# 默认是升序
# [-21, -12, 5, 9, 36]

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# 例如按绝对值大小排序：
print(sorted([36, 5, -12, 9, -21], key=abs))
# [5, 9, -12, -21, 36]
# key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。

# 对比原始的list和经过key=abs处理过的list：
# list = [36, 5, -12, 9, -21]
# keys = [36, 5,  12, 9,  21]

# 然后sorted()函数按照keys进行排序，并按照对应关系返回list相应的元素：
# keys排序结果 => [5, 9,  12,  21, 36]
# 最终结果     => [5, 9, -12, -21, 36]


print(sorted(['bob', 'about', 'Zoo', 'Credit']))
# ['Credit', 'Zoo', 'about', 'bob']
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。

# 排序应该忽略大小写，按照字母序排序。
# 要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。
# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))  # ['about', 'bob', 'Credit', 'Zoo']
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.upper))  # ['about', 'bob', 'Credit', 'Zoo']


# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))
# ['Zoo', 'Credit', 'bob', 'about']