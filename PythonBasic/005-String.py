# !/usr/bin/python3

# var1 = 'Hello World!'
# var2 = "IlovePython"
#
# print("var1[0]: ", var1[0])
# print("var2[1:5]: ", var2[1:5])
#
# # 执行结果：
# var1[0]:  H
# var2[1:5]:  love
#
# # 字符串的更新
# var1 = 'hello world'
# print('更新字符串为：', var1[:6] + 'huangkeke')
#
# # 执行结果
# 更新字符串为： hello huangkeke

# # 字符串的截取
# var1 = 'hi,my name is huangkeke'
#
# print('var1[0: 2]', var1[0: 2])  #指定开始，结束位置    截取包括开始位置，不包括结束位置
# print('var1[:]', var1[:])        #截取全部
# print('var1[:6]', var1[:6])      #截取该字符串开始头位置到第6个位置
# print('var1[2:]', var1[2:])      #截取该字符串从第2位置到结束位置
# print('var1[::2]', var1[::2])    #截取从头到尾，步长为2


# 转义字符
# a = "Hello"
# b = "Python"
#
# print("a + b 输出结果：", a + b)
# print("a * 2 输出结果：", a * 2)
# print("a[1] 输出结果：", a[1])
# print("a[1:4] 输出结果：", a[1:4])
#
# if ("H" in a):
#     print("H 在变量 a 中")
# else:
#     print("H 不在变量 a 中")
#
# if ("M" not in a):
#     print("M 不在变量 a 中")
# else:
#     print("M 在变量 a 中")
#
# print(r'\n')
# print(R'\n')
#
# # 执行结果
# a + b 输出结果： HelloPython
# a * 2 输出结果： HelloHello
# a[1] 输出结果： e
# a[1:4] 输出结果： ell
# H 在变量 a 中
# M 不在变量 a 中
# \n
# \n

# Python字符串格式化
# print ("我叫 %s 今年 %d 岁!" % ('小明', 10))
#
# # 执行结果
# 我叫 小明 今年 10 岁!

# # format格式化函数
# print("姓名：{name}, 年龄 {age}".format(name="huangkeke", age=24))
#
# # 通过字典设置参数
# site = {"name": "huangkeke", "age": 24}
# print("姓名：{name}, 年龄 {age}".format(**site))
#
# # 通过列表索引设置参数
# my_list = ['huangkeke', 24]
# print("姓名：{0[0]}, 年龄 {0[1]}".format(my_list))  # "0" 是可选的
#
# # 执行结果
# 姓名：huangkeke, 年龄 24
# 姓名：huangkeke, 年龄 24
# 姓名：huangkeke, 年龄 24


# # 三引号
#
# para_str = """这是一个多行字符串的实例
# 多行字符串可以使用制表符
# TAB ( \t )。
# 也可以使用换行符 [ \n ]。
# """
# print (para_str)
#
# # 执行结果
# 这是一个多行字符串的实例
# 多行字符串可以使用制表符
# TAB ( 	 )。
# 也可以使用换行符 [
#  ]。
