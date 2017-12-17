#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : highs_lows.py
# @Author: huangkeke
# @Date  : 2017/12/12
# @Contact : hkkhuang@163.com

"""
访问并可视化以两种常见格式存储的数据： CSV和JSON。
我们将使用Python模块csv来处理以CSV（逗号分隔的值）格式存储
的天气数据，找出两个不同地区在一段时间内的最高温度和最低温
度。然后，我们将使用matplotlib根据下载的数据创建一个图表，展
示两个不同地区的气温变化：阿拉斯加锡特卡和加利福尼亚死亡谷。
"""

# 要在文本文件中存储数据，最简单的方式是将数据作为一系列以逗号分隔的值（CSV）写入文件。这样的文件称为CSV文件。

# csv模块包含在Python标准库中，可用于分析CSV文件中的数据行，让我们能够快速提取感兴趣的值。

# [1]
# import csv
#
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as file_object:  # 打开文件 将结果存放到文件对象file_object中
#
#     # 调用csv.reader(),并将存储的文件对象传递
#     # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
#     reader = csv.reader(file_object)  # 创建一个阅读器对象
#     header_row = next(reader)  # 使用next()函数   返回文件的下一行
#     # 这里我们只调用next()一次  相当于获取到  标题头
#     print(header_row)
#
# # ['AKDT', 'Max TemperatureF', 'Mean TemperatureF', 'Min TemperatureF', 'Max Dew PointF', 'MeanDew PointF',
# #  'Min DewpointF', 'Max Humidity', ' Mean Humidity', ' Min Humidity', ' Max Sea Level PressureIn',
# #  ' Mean Sea Level PressureIn', ' Min Sea Level PressureIn', ' Max VisibilityMiles', ' Mean VisibilityMiles',
# #  ' Min VisibilityMiles', ' Max Wind SpeedMPH', ' Mean Wind SpeedMPH', ' Max Gust SpeedMPH', 'PrecipitationIn',
# #  ' CloudCover', ' Events', ' WindDirDegrees']


# # [2] 打印文件头及其位置
# import csv
#
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as file_object:
#     reader = csv.reader(file_object)  # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
#     header_row = next(reader)
#
#     for index, column_header in enumerate(header_row):  # 对列表调用了enumerate()来获取每个元素的索引及其值
#         print(index, column_header)
#
# # 从中可知，日期和最高气温分别存储在第0列和第1列。
# # 为研究这些数据，我们将处理 sitka_weather_07 - 2014.csv中的每行数据，并提取其中索引为0和1的值。
#
# # 0 AKDT
# # 1 Max TemperatureF
# # 2 Mean TemperatureF
# # 3 Min TemperatureF
# # ...
# #
# # 20  CloudCover
# # 21  Events
# # 22  WindDirDegrees


# [3]提取并读取数据
# import csv
#
# # 从文件中获取最高气温
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as file_object:
#     reader = csv.reader(file_object)  # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
#     # print(reader)  # <_csv.reader object at 0x103741278>
#     header_row = next(reader)
#
#     highs = []  # 存储每天最高气温
#     for row in reader:
#         highs.append(row[1])
#
#     print(highs)
# #
# ['64', '71', '64', '59', '69', '62', '61', '55', '57', '61', '57', '59', '57', '61', '64', '61', '59', '63', '60',
# '57', '69', '63', '62', '59', '57', '57', '61', '59', '61', '61', '66']


# # [4]提取并读取数据-将读取字符串转换为int类型
# import csv
#
# # 从文件中获取最高气温
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as file_object:
#     reader = csv.reader(file_object)  # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
#     # print(reader)  # <_csv.reader object at 0x103741278>
#     header_row = next(reader)
#
#     highs = []  # 存储每天最高气温
#     for row in reader:
#         high = int(row[1])  # 使用int()将字符串转换为数字
#         highs.append(high)
#
#     print(highs)
#
# # [64, 71, 64, 59, 69, 62, 61, 55, 57, 61, 57, 59, 57, 61, 64, 61, 59, 63, 60, 57, 69,
# # 63, 62, 59, 57, 57, 61, 59, 61, 61, 66]

# # [4]提取并读取数据-绘制图像
# import csv
# from matplotlib import pyplot as plt
#
# # 从文件中获取最高气温
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as file_object:
#     reader = csv.reader(file_object)  # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
#     # print(reader)  # <_csv.reader object at 0x103741278>
#     header_row = next(reader)
#
#     highs = []  # 存储每天最高气温
#     for row in reader:
#         high = int(row[1])  # 使用int()将字符串转换为数字
#         highs.append(high)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(highs, c='red')
#
# # 设置图形的格式
# plt.title('Daily high temperatures', fontsize=24)
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Temperature(F)', fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()

# [4]提取并读取数据-绘制图像 最高-最低气温
# import csv
# from matplotlib import pyplot as plt
#
# # 从文件中获取最高气温
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as file_object:
#     reader = csv.reader(file_object)  # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
#     # print(reader)  # <_csv.reader object at 0x103741278>
#     header_row = next(reader)
#
#     highs = []  # 存储每天最高气温
#     lows = []
#     for row in reader:
#         high = int(row[1])  # 使用int()将字符串转换为数字
#         low = int(row[3])  # 使用int()将字符串转换为数字
#         highs.append(high)
#         lows.append(low)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(highs, c='red')
# plt.plot(lows, c='green')
#
# # 设置图形的格式
# plt.title('Daily high temperatures', fontsize=24)
# plt.xlabel('Date', fontsize=14)
# plt.ylabel('Temperature(F)', fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()


# import csv
# from matplotlib import pyplot as plt
# from datetime import datetime
#
# # 从文件中获取最高气温
# filename = 'sitka_weather_07-2014.csv'
# with open(filename) as file_object:
#     reader = csv.reader(file_object)  # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
#     # print(reader)  # <_csv.reader object at 0x103741278>
#     header_row = next(reader)
#
#     dates, highs = [], []  # 存储日期 + 每天最高气温
#     lows = []
#     for row in reader:
#         current_date = datetime.strptime(row[0], "%Y-%m-%d")
#         dates.append(current_date)
#
#         high = int(row[1])  # 使用int()将字符串转换为数字
#         highs.append(high)
#
# # 根据数据绘制图形
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red')
#
# # 设置图形的格式
# plt.title('Daily high temperatures', fontsize=24)
# plt.xlabel('Date', fontsize=14)
# fig.autofmt_xdate()  # 绘制斜的日期标签
# plt.ylabel('Temperature(F)', fontsize=14)
# plt.tick_params(axis='both', which='major', labelsize=10)
#
# plt.show()

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取最高气温
filename = 'sitka_weather_07-2014.csv'
with open(filename) as file_object:
    reader = csv.reader(file_object)  # reader处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中
    # print(reader)  # <_csv.reader object at 0x103741278>
    header_row = next(reader)

    dates = []
    highs = []  # 存储每天最高气温
    lows = []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)
        high = int(row[1])  # 使用int()将字符串转换为数字
        highs.append(high)
        low = int(row[3])  # 使用int()将字符串转换为数字
        lows.append(low)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.6)
plt.plot(dates, lows, c='green', alpha=0.6)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title('Daily high and low temperatures', fontsize=24)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Temperature(F)', fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=10)

plt.show()


# import csv
# from datetime import datetime
#
# from matplotlib import pyplot as plt
#
# # Get dates, high, and low temperatures from file.
# filename = 'death_valley_2014.csv'
# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)
#
#     dates, highs, lows = [], [], []
#     for row in reader:
#         try:
#             current_date = datetime.strptime(row[0], "%Y-%m-%d")
#             high = int(row[1])
#             low = int(row[3])
#         except ValueError:
#             print(current_date, 'missing data')
#         else:
#             dates.append(current_date)
#             highs.append(high)
#             lows.append(low)
#
# # Plot data.
# fig = plt.figure(dpi=128, figsize=(10, 6))
# plt.plot(dates, highs, c='red', alpha=0.5)
# plt.plot(dates, lows, c='blue', alpha=0.5)
# plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#
# # Format plot.
# title = "Daily high and low temperatures - 2014\nDeath Valley, CA"
# plt.title(title, fontsize=20)
# plt.xlabel('', fontsize=16)
# fig.autofmt_xdate()
# plt.ylabel("Temperature (F)", fontsize=16)
# plt.tick_params(axis='both', which='major', labelsize=16)
#
# plt.show()