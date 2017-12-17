#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : random_walk.py
# @Author: huangkeke
# @Date  : 2017/12/12
# @Contact : hkkhuang@163.com

# 随机漫步是这样行走得到的路径：每次行走都完全是随机的，没有明确的方向，
# 结果是由一系列随机决策决定的。你可以这样认为，随机漫步就是蚂蚁在晕头转向的情况下，每次都沿随机的方向前行所经过的路径。
# 在自然界、物理学、生物学、化学和经济领域，随机漫步都有其实际用途。例如，漂浮在水
# 滴上的花粉因不断受到水分子的挤压而在水面上移动。水滴中的分子运动是随机的，因此花粉在
# 水面上的运动路径犹如随机漫步。我们稍后将编写的代码模拟了现实世界的很多情形。

from random import choice

class RandomWalk():
    """一个生产随机漫步数据的类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步属性"""
        self.num_points = num_points  # 产生点个数

        # 所有的随机种子都始于(0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的所有点"""

        # 不断漫步,直到列表达到指定长度 循环不断运行，直到漫步包含所需数量的点
        while len(self.x_values) < self.num_points:
            # 决定前进的方向以及沿这个方向前进的距离
            # 使用choice([1, -1])给x_direction选择一个值，结果要么是表示向右走的1，要么是表示向左走的-1
            x_direction = choice([1, -1])

            # choice([0, 1, 2, 3, 4])随机地选择一个0~4之间的整数，告诉Python 沿指定的方向走多远（x_distance）。
            x_distance = choice([0, 1, 2, 3, 4])

            # 移动方向乘以移动距离，以确定沿x和y轴移动的距离。如果x_step为正，将向右移动，为负将向左移动，而为零将垂直移动；
            x_step = x_direction * x_distance

            # 如果y_step为正，就意味着向上移动，为负
            # 意味着向下移动，而为零意味着水平移动。如果x_step和y_step都为零，则意味着原地踏步，我
            # 们拒绝这样的情况，接着执行下一次循环

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # 为获取漫步中下一个点的x值，我们将x_step与x_values中的最后一个值相加
            # 得下一个点的x值和y值后，我们将它们分别附加到列表x_values和y_values的末尾。
            self.x_values.append(next_x)
            self.y_values.append(next_y)


