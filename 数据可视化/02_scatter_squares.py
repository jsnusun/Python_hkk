#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : 02_scatter_squares.py
# @Author: huangkeke
# @Date  : 2017/12/12
# @Contact : hkkhuang@163.com

"""使用scatter绘制散点图并设置其样式"""
# [1]
# import matplotlib.pyplot as plt
#
# plt.scatter(2, 4)
# plt.show()

# 有时候，需要绘制散点图并设置各个数据点的样式。例如，你可能想以一种颜色显示较小的
# 值，而用另一种颜色显示较大的值。绘制大型数据集时，你还可以对每个点都设置同样的样式，
# 再使用不同的样式选项重新绘制某些点，以突出它们。

# # [2]
# import matplotlib.pyplot as plt
#
# plt.scatter(2, 4, s=200)  # 实参s 设置绘制图形时候的点的尺寸
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记大小
# plt.tick_params(axis='both', which='major', labelsize=8)
# plt.show()

# # [3] 绘制一系列点
# import matplotlib.pyplot as plt
#
# # 要绘制一系列的点，可向scatter()传递两个分别包含x值和y值的列表
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.scatter(x_values,y_values, s=100)  # 实参s 设置绘制图形时候的点的尺寸
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置刻度标记大小
# plt.tick_params(axis='both', which='major', labelsize=10)
# plt.show()


# [4] 自动计算数据  绘制一系列点
# import matplotlib.pyplot as plt
#
# # 要绘制一系列的点，可向scatter()传递两个分别包含x值和y值的列表
# x_values = list(range(1, 1001))  # 创建一个包含x值的列表
# y_values = [x**2 for x in x_values]  # 通过列表解析 遍历x值 计算x**2 将结果存放到y_values列表中
#
# plt.scatter(x_values, y_values, s=20)  # 实参s 设置绘制图形时候的点的尺寸
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=10)
#
# # 设置每个坐标轴的取值范围
# # axis()函数需要提供四个参数 x,y坐标轴的最小值和最大值
# plt.axis([0, 1100, 0, 1100000])  # 使用函数axis() 指定每个坐标轴的取值范围
#
# plt.show()


# # [5] 自动计算数据  绘制一系列点  并删除数据点的轮廓
# import matplotlib.pyplot as plt
#
# # 要绘制一系列的点，可向scatter()传递两个分别包含x值和y值的列表
# x_values = list(range(1, 1001))  # 创建一个包含x值的列表
# y_values = [x**2 for x in x_values]  # 通过列表解析 遍历x值 计算x**2 将结果存放到y_values列表中
#
# # matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，在散点图包含的
# # 数据点不多时效果很好。但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，
# # 可在调用scatter()时传递实参edgecolor='none'
# plt.scatter(x_values, y_values, edgecolors='none', s=20)  # 实参s 设置绘制图形时候的点的尺寸
# # plt.scatter(x_values, y_values, s=20)  # 实参s 设置绘制图形时候的点的尺寸
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置每个坐标轴的取值范围
# # axis()函数需要提供四个参数 x,y坐标轴的最小值和最大值
# plt.axis([0, 1100, 0, 1100000])  # 使用函数axis() 指定每个坐标轴的取值范围
#
# plt.show()


# [6] 自动计算数据  绘制一系列点  并删除数据点的轮廓  修改默认颜色
# import matplotlib.pyplot as plt
#
# # 要绘制一系列的点，可向scatter()传递两个分别包含x值和y值的列表
# x_values = list(range(1, 100))  # 创建一个包含x值的列表
# y_values = [x**2 for x in x_values]  # 通过列表解析 遍历x值 计算x**2 将结果存放到y_values列表中
#
# # matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，在散点图包含的
# # 数据点不多时效果很好。但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，
# # 可在调用scatter()时传递实参edgecolor='none'
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=20)  # 实参s 设置绘制图形时候的点的尺寸
#
# # 还可以使用RGB颜色模式自定义颜色。要指定自定义颜色，可传递参数c，并将其设置为一个元组，
# # 其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。
# # 值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置每个坐标轴的取值范围
# # axis()函数需要提供四个参数 x,y坐标轴的最小值和最大值
# plt.axis([0, 110, 0, 11000])  # 使用函数axis() 指定每个坐标轴的取值范围
#
# plt.show()

#
# # [7] 自动计算数据  绘制一系列点  并删除数据点的轮廓  使用颜色映射
# # 颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。在可视化中，颜色
# # 映射用于突出数据的规律，例如，你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。
# # 模块pyplot内置了一组颜色映射。要使用这些颜色映射，你需要告诉pyplot该如何设置数据
# # 集中每个点的颜色。
# #
# # 下面演示了如何根据每个点的y值来设置其颜色：
# import matplotlib.pyplot as plt
#
# # 要绘制一系列的点，可向scatter()传递两个分别包含x值和y值的列表
# x_values = list(range(1, 1001))  # 创建一个包含x值的列表
# y_values = [x**2 for x in x_values]  # 通过列表解析 遍历x值 计算x**2 将结果存放到y_values列表中
#
# # matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，在散点图包含的
# # 数据点不多时效果很好。但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，
# # 可在调用scatter()时传递实参edgecolor='none'
# plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=20)  # 实参s 设置绘制图形时候的点的尺寸
#
# # 还可以使用RGB颜色模式自定义颜色。要指定自定义颜色，可传递参数c，并将其设置为一个元组，
# # 其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。
# # 值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
# #
# # 将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。这些代
# # 码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色
#
# # 设置图表标题并给坐标轴加上标签
# plt.title("Square Numbers", fontsize=24)
# plt.xlabel("Value", fontsize=14)
# plt.ylabel("Square of Value", fontsize=14)
#
# # 设置每个坐标轴的取值范围
# # axis()函数需要提供四个参数 x,y坐标轴的最小值和最大值
# plt.axis([0, 1100, 0, 1100000])  # 使用函数axis() 指定每个坐标轴的取值范围
#
# plt.show()



# [8] 自动计算数据  绘制一系列点  并删除数据点的轮廓  使用颜色映射  自动保存图标
# 颜色映射（colormap）是一系列颜色，它们从起始颜色渐变到结束颜色。在可视化中，颜色
# 映射用于突出数据的规律，例如，你可能用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。
# 模块pyplot内置了一组颜色映射。要使用这些颜色映射，你需要告诉pyplot该如何设置数据
# 集中每个点的颜色。
#
# 下面演示了如何根据每个点的y值来设置其颜色何根据每个点的y值来设置其颜色：
import matplotlib.pyplot as plt

# 要绘制一系列的点，可向scatter()传递两个分别包含x值和y值的列表
x_values = list(range(1, 1001))  # 创建一个包含x值的列表
y_values = [x**2 for x in x_values]  # 通过列表解析 遍历x值 计算x**2 将结果存放到y_values列表中

# matplotlib允许你给散点图中的各个点指定颜色。默认为蓝色点和黑色轮廓，在散点图包含的
# 数据点不多时效果很好。但绘制很多点时，黑色轮廓可能会粘连在一起。要删除数据点的轮廓，
# 可在调用scatter()时传递实参edgecolor='none'
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=20)  # 实参s 设置绘制图形时候的点的尺寸

# 还可以使用RGB颜色模式自定义颜色。要指定自定义颜色，可传递参数c，并将其设置为一个元组，
# 其中包含三个0~1之间的小数值，它们分别表示红色、绿色和蓝色分量。
# 值越接近0，指定的颜色越深，值越接近1，指定的颜色越浅。
#
# 将参数c设置成了一个y值列表，并使用参数cmap告诉pyplot使用哪个颜色映射。这些代
# 码将y值较小的点显示为浅蓝色，并将y值较大的点显示为深蓝色

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=10)

# 设置每个坐标轴的取值范围
# axis()函数需要提供四个参数 x,y坐标轴的最小值和最大值
plt.axis([0, 1100, 0, 1100000])  # 使用函数axis() 指定每个坐标轴的取值范围

plt.show()

# 要让程序自动将图表保存到文件中，可将对plt.show()的调用替换为对plt.savefig()的调用
plt.savefig('squares_plot.png', bbox_inches='tight')
# 第一个实参指定要以什么样的文件名保存图表，这个文件将存储到scatter_squares.py所在的
# 目录中；第二个实参指定将图表多余的空白区域裁剪掉。如果要保留图表周围多余的空白区域，
# 可省略这个实参。
