#!/usr/bin/python3

# n = 100
# sumTotal = 0
# counter = 1
# while counter <= n:
#     sumTotal += counter
#     counter += 1
#
# print('1+2+...+100=',sumTotal)
#
# # 执行结果:
# 1+2+...+100= 5050

#
# count = 0
# while count < 5:
#     print(count, " 小于 5")
#     count = count + 1
# else:
#     print(count, " 大于或等于 5")
#
# 执行条件:
# 0  小于 5
# 1  小于 5
# 2  小于 5
# 3  小于 5
# 4  小于 5
# 5  大于或等于 5
#
# languages = ['C', 'C++', 'Java', 'Python']
# for x in languages:
#     print(x)
#
# # 执行结果:
# C
# C++
# Java
# Python
#
# sites = ["Baidu", "Google", "YZU", "Taobao"]
# for site in sites:
#     if site == "YZU":
#         print("扬州大学!")
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")
#
# # 执行结果:
# 循环数据 Baidu
# 循环数据 Google
# 循环数据 yzu.com
# 循环数据 Taobao
# 没有循环数据!
# 完成循环!
#
# for i in range(5):
#     print(i)
#
# 执行结果:
# 0
# 1
# 2
# 3
# 4
#
# for i in range(5,9):
#     print(i)
#
# 执行结果:
# 5
# 6
# 7
# 8
#
# for i in range(0, 10, 3):
#     print(i)
#
# 执行结果:
# 0
# 3
# 6
# 9

#
# for i in range(-10, -100, -30):
#     print(i)
#
# # 执行结果:
# -10
# -40
# -70
#
# a = ['Google', 'Baidu', 'YZU', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i, a[i])
#
# # 执行结果:
# 0 Google
# 1 Baidu
# 2 YZU
# 3 Taobao
# 4 QQ
#
# a = list(range(5))
# print(a)
#
# # 执行结果:
# [0, 1, 2, 3, 4]


# for letter in 'Huangkeke':  # 第一个实例
#     if letter == 'g':
#         break
#     print('当前字母为 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     print('当期变量值为 :', var)
#     var = var - 1
#     if var == 5:
#         break
#
# print("Good bye!")
#
# # 执行结果:
# 当前字母为 : H
# 当前字母为 : u
# 当前字母为 : a
# 当前字母为 : n
# 当期变量值为 : 10
# 当期变量值为 : 9
# 当期变量值为 : 8
# 当期变量值为 : 7
# 当期变量值为 : 6
# Good bye!


#
# for letter in 'Huangkeke':  # 第一个实例
#     if letter == 'o':  # 字母为 o 时跳过输出
#         continue
#     print('当前字母 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:  # 变量为 5 时跳过输出
#         continue
#     print('当前变量值 :', var)
# print("Good bye!")
#
# # 执行结果:
# 当前字母 : H
# 当前字母 : u
# 当前字母 : a
# 当前字母 : n
# 当前字母 : g
# 当前字母 : k
# 当前字母 : e
# 当前字母 : k
# 当前字母 : e
# 当前变量值 : 9
# 当前变量值 : 8
# 当前变量值 : 7
# 当前变量值 : 6
# 当前变量值 : 4
# 当前变量值 : 3
# 当前变量值 : 2
# 当前变量值 : 1
# 当前变量值 : 0
# Good bye!
#
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, '等于', x, '*', n//x)
#             break
#     else:
#         # 循环中没有找到元素
#         print(n, ' 是质数')
#
# # 执行结果:
# 2  是质数
# 3  是质数
# 4 等于 2 * 2
# 5  是质数
# 6 等于 2 * 3
# 7  是质数
# 8 等于 2 * 4
# 9 等于 3 * 3

#
# for letter in 'Huangkeke':
#     if letter == 'g':
#         pass
#         print('执行 pass 块')
#     print('当前字母 :', letter)
#
# print("Good bye!")
#
# 执行结果:
# 当前字母 : H
# 当前字母 : u
# 当前字母 : a
# 当前字母 : n
# 执行 pass 块
# 当前字母 : g
# 当前字母 : k
# 当前字母 : e
# 当前字母 : k
# 当前字母 : e
# Good bye!