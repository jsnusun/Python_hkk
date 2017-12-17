#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 01_mpl_squares.py
# @Author: huangkeke
# @Date  : 2017/12/12
# @Contact : hkkhuang@163.com

# import matplotlib.pyplot as plt
# import numpy as np
#
# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)
#
# # Note that using plt.subplots below is equivalent to using
# # fig = plt.figure and then ax = fig.add_subplot(111)
# fig, ax = plt.subplots()
# ax.plot(t, s)
#
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()
#
# fig.savefig("test.png")
# plt.show()

# [1]
# import matplotlib.pyplot as plt  # 导入模块pyplot 指定别名plt
#
# squares = [1, 4, 9, 16, 25]  # 创建一个列表 存储平方数
# plt.plot(squares)  # 函数尝试根据这些数字绘制出有意义的图形  参数为上述列表
# plt.show()  # 打开matplotlib 查看器,并显示绘制的图形


# [2]
# import matplotlib.pyplot as plt  # 导入模块pyplot 指定别名plt
#
# squares = [1, 4, 9, 16, 25]  # 创建一个列表 存储平方数
# plt.plot(squares, linewidth=5)  # 参数linewidth决定了plot()绘制的线条的粗细
#
# # 设置图标标题,并给坐标轴添加标签
# plt.title('Square Number', fontsize=24)  # 函数title()给定绘制图标的标题
# plt.xlabel('Value', fontsize=14)  # xlabel()函数为x轴设置标题
# plt.ylabel('Square of Value', fontsize=14) # ylabel()函数为y轴设置标题
#
# # 设置刻度标记大小
# plt.tick_params(axis='both', labelsize=14)  # 函数tick_params()设置刻度样式 实参axis=''设置刻度 labelsize设置字号
#
# plt.show()  # 打开matplotlib 查看器,并显示绘制的图形


[3]
import matplotlib.pyplot as plt  # 导入模块pyplot 指定别名plt

# 当你向plot()提供一系列数字时，它假设第一个数据点对应的x坐标值为0，但我们的第一个
# 点对应的x值为1。为改变这种默认行为，我们可以给plot()同时提供输入值和输出值：

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]  # 创建一个列表 存储平方数
plt.plot(input_value, squares, linewidth=5)  # 参数linewidth决定了plot()绘制的线条的粗细

# 设置图标标题,并给坐标轴添加标签
plt.title('Square Number', fontsize=24)  # 函数title()给定绘制图标的标题
plt.xlabel('Value', fontsize=14)  # xlabel()函数为x轴设置标题
plt.ylabel('Square of Value', fontsize=14) # ylabel()函数为y轴设置标题

# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=14)  # 函数tick_params()设置刻度样式 实参axis=''设置刻度 labelsize设置字号

plt.show()  # 打开matplotlib 查看器,并显示绘制的图形


