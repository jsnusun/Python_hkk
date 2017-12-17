#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 03_rw_visual.py
# @Author: huangkeke
# @Date  : 2017/12/12
# @Contact : hkkhuang@163.com

# [1]
# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# # 创建一个randomWalk实例  并将其中包含的点都绘制出来
#
# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, s=5)
# plt.show()

#
# # [2] 模拟多次随机漫步
# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# # 只要程序处于活动状态,就不断的模拟随机漫步
# while True:
#     # 创建一个randomWalk实例  并将其中包含的点都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#     plt.scatter(rw.x_values, rw.y_values, s=5)
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n)')
#     if keep_running == 'n':
#         break
#
# 这些代码模拟一次随机漫步，在matplotlib查看器中显示结果，再在不关闭查看器的情况下暂
# 停。如果你关闭查看器，程序将询问你是否要再模拟一次随机漫步。如果你输入y，可模拟多次
# 随机漫步：这些随机漫步都在起点附近进行，大多沿特定方向偏离起点，漫步点分布不均匀等




# # [3] 模拟多次随机漫步  设置漫步图的样式
# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# # 只要程序处于活动状态,就不断的模拟随机漫步
# while True:
#     # 创建一个randomWalk实例  并将其中包含的点都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n)')
#     if keep_running == 'n':
#         break


# # [4] 重新绘制起点和终点
# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# # 只要程序处于活动状态,就不断的模拟随机漫步
# while True:
#     # 创建一个randomWalk实例  并将其中包含的点都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
#
#     # 突出起点和终点
#     plt.scatter(0, 0, c='green', edgecolors='none', s=50)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n)')
#     if keep_running == 'n':
#         break


# [5] 重新绘制起点和终点-隐藏坐标轴
# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# # 只要程序处于活动状态,就不断的模拟随机漫步
# while True:
#     # 创建一个randomWalk实例  并将其中包含的点都绘制出来
#     rw = RandomWalk()
#     rw.fill_walk()
#
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=5)
#
#     # 突出起点和终点
#     plt.scatter(0, 0, c='green', edgecolors='none', s=50)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
#
#     # 隐藏坐标轴
#     plt.axes().get_xaxis().set_visible(False)  # 使用函数 plt.axes()
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n)')
#     if keep_running == 'n':
#         break


# # [5] 重新绘制起点和终点-隐藏坐标轴-增加点数
# import matplotlib.pyplot as plt
#
# from random_walk import RandomWalk
#
# # 只要程序处于活动状态,就不断的模拟随机漫步
# while True:
#     # 创建一个randomWalk实例  并将其中包含的点都绘制出来
#     rw = RandomWalk(50000)
#     rw.fill_walk()
#
#     point_numbers = list(range(rw.num_points))
#     plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)
#
#     # 突出起点和终点
#     plt.scatter(0, 0, c='green', edgecolors='none', s=50)
#     plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)
#
#     # 隐藏坐标轴
#     plt.axes().get_xaxis().set_visible(False)  # 使用函数 plt.axes()
#     plt.axes().get_yaxis().set_visible(False)
#
#     plt.show()
#
#     keep_running = input('Make another walk? (y/n)')
#     if keep_running == 'n':
#         break


# [6] 重新绘制起点和终点-隐藏坐标轴-增加点数-调整尺寸以适合屏幕
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态,就不断的模拟随机漫步
while True:
    # 创建一个randomWalk实例  并将其中包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    # 函数figure()用于指定图表的宽度、高度、分辨率和背景色。你需要给形参figsize指定一个元组，向matplotlib指出绘图窗口的尺寸，单位为英寸。

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=50)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=50)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)  # 使用函数 plt.axes()
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n)')
    if keep_running == 'n':
        break
