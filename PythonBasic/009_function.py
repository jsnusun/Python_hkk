#!/usr/bin/python3

# 1----------------------------------
# # 定义函数
# def hello():
#     print('hello world')
#
# # 调用函数
# hello()
#
# # 输出结果
# # hello world

# 2----------------------------------
# # 带参数的函数
# # 计算面积函数
# def area(width, height):
#     return width * height
#
# width = int(input('请输入width: '))
# height = int(input('请输入height: '))
#
# myArea = area(width, height)  # 传递参数width,height
# print('width:%d, height:%d, area:%d' % (width, height, myArea))

# # 执行结果
# 请输入width: 4
# 请输入height: 5
# width:4, height:5, area:20

# 3----------------------------------
# a = 4  # 创建一个对象 4  变量a 指向这个对象
# b = a  # 创建一个变量b 指向a指向的对象
# a = 6  # 重新创建一个int对象 6,变量a指向对象6
# print('a = ',a)  # 打印输出变量a  结果是6  将之前指向的对象4抛弃,重现指向值得对象6
# print('b = ',b)  # 打印输出变量b  结果是4  b在a改变指向时不受影响,还是指向之前的对象4
#
# # 执行结果:
# # a =  6
# # b =  4

# 4----------------------------------
# 函数的调用
# def printStr(str):
#     print(str)  # 将传入的字符串打印输出
#     return;
#
# # 调用函数
# printStr('将传入的字符串打印输出')
#
# # 再调用这个函数
# printStr('再次调用这个函数,将传入字符串打印输出')

# 执行结果:
# 将传入的字符串打印输出
# 再次调用这个函数,将传入字符串打印输出

# 5----------------------------------
# # 传递不可改变类型
# def changeInt(a):
#     print('传递到函数内的值为: ', a)
#     a = 10
#     print('改变后的的值为: ', a)
#
#
#
# b = 2
# changeInt(b)
#
# print('调用函数后b = ', b)  # 调用函数changeInt() 对变量b没有影响
#
# # 执行结果:
# # 传递到函数内的值为:  2
# # 改变后的的值为:  10
# # 调用函数后b =  2

# 6----------------------------------
# # 传递可变参数
# def changecara(mylist):
#     print("传递到函数值:", mylist)
#     mylist.append([1, 2, 3])
#     print("函数内操作后取值:", mylist)
#     return
#
#
# # 调用函数:
# mylist = [11, 22, 33]
# print('myList原始取值:', mylist)
#
# changecara(mylist)
# print('调用函数后myList取值:', mylist)
# #
# # 执行结果:
# # myList原始取值: [11, 22, 33]
# # 传递到函数值: [11, 22, 33]
# # 函数内操作后取值: [11, 22, 33, [1, 2, 3]]
# # 调用函数后myList取值: [11, 22, 33, [1, 2, 3]]

# 7----------------------------------
# # 必须参数
# def printStr(str):
#     print(str)
#     return
#
# printStr()
#
# # 调用时没有传递参数, 有语法错误
# # Traceback (most recent call last):
# #   File "/Users/hkkhuang/Documents/Python/PythonBasic/009_function.py", line 100, in <module>
# #     printStr()
# # TypeError: printStr() missing 1 required positional argument: 'str'


# def printStr(str, name, age):
#     print(str)
#     return
#
# printStr('必须参数,在调用时要求必须传递参数,并且要求传入参数的顺序,数量与声明都要相同')
#
# # Traceback (most recent call last):
# #   File "/Users/hkkhuang/Documents/Python/PythonBasic/009_function.py", line 113, in <module>
# #     printStr('必须参数,在调用时要求必须传递参数,并且要求传入参数的顺序,数量与声明都要相同')
# # TypeError: printStr() missing 2 required positional arguments: 'name' and 'age'
#
# def printStr(str, name, age):
#     print(str, name, age)
#     return
#
# printStr('必须参数,在调用时要求必须传递参数,并且要求传入参数的顺序,数量与声明都要相同', 'zhangsan', 22)
#
# # 执行结果
# # 必须参数,在调用时要求必须传递参数,并且要求传入参数的顺序,数量与声明都要相同 zhangsan 22


# 8----------------------------------
# # 关键字参数
# def printStr(str):
#     print(str)
#     return
#
#
# # 调用printme函数
# printStr(str="关键字参数")
#
# # 执行结果:
# # 关键字参数
#
# def printStr(name, gender, age):
#     print(name, gender, age)
#     return
#
#
# # 调用printme函数
# printStr(name="zhangsan", age=18, gender='M')
#
# # 执行结果:
# # zhangsan M 18

# 9----------------------------------
# # 默认参数
# def printInfo(name, age=18):
#     print('name:',name, 'age:', age)
#
#
# printInfo(name='lisi', age=22)
# printInfo(age=22, name='lisi')
# printInfo(name='lisi')
# printInfo('zhangsan', 22)
# printInfo(22, 'zhangsan')
# # 执行结果:
# # name: lisi age: 22
# # name: lisi age: 22
# # name: lisi age: 18
# # name: zhangsan age: 22
# # name: 22 age: zhangsan

# 10----------------------------------
# # 不定长参数
# def printInfo(arg1, *vartuple):
#     print('输出')
#     print(arg1)
#
#     for var in vartuple:
#         print(var)
#
#     return
#
# printInfo(10)
# printInfo(10, 20, 30, 40)
#
# # 执行结果:
# # 输出
# # 10
# # 输出
# # 10
# # 20
# # 30
# # 40
#
# # 不定长参数
# def printInfo(arg1, *vartuple):
#     print('输出')
#     #print(arg1)  #这是第一个参数
#
#     for var in vartuple:
#         print(var)
#
#     return
#
# printInfo(10)
# printInfo(10, 20, 30, 40)
#
# # 执行结果:
# # 输出
# # 输出
# # 20
# # 30
# # 40

#
# # 不定长参数
# def printInfo(*vartuple):
#     print('输出')
#     #print(arg1)  #这是第一个参数
#
#     for var in vartuple:
#         print(var)
#
#     return
#
#
# printInfo(1, 2, 3, 4)
#
# # 执行结果:
# # 输出
# # 1
# # 2
# # 3
# # 4


# # 不定长参数
# def printInfo(*vartuple):
#
#     if len(vartuple) == 0:  # 判断元组是否为空
#         print('没有传入参数')
#         return
#     else:
#         print('输出')
#         for var in vartuple:
#             print(var)
#
#     return
#
#
# printInfo()  # 调用时没有传递参数,就是一个空元组
#
# # 执行结果:
# # 没有传入参数


# 11----------------------------------
# 匿名函数
# sum = lambda arg1, arg2: arg1 + arg2
#
#
# # 调用sum函数
# print('相加后的值为:', sum(1, 2))
# print('相加后的值为:', sum(10, 20))

# 执行结果:
# 相加后的值为: 3
# 相加后的值为: 30


# 12----------------------------------
# # return 返回语句
# def sum(arg1, arg2):
#     total = arg1 + arg2
#     print('函数内和为:', total)
#     return total
#
#
# total = sum(1, 2)
# print('函数外和为:', total)

# 执行结果:
# 函数内和为: 3
# 函数外和为: 3


# 13 ----------------------------------
# # 变量作用域
# x = int(2.7)   # 内建作用域
# print(x)
# g_count = 0  # 全局作用域
#
# def outer():
#     o_count = 1  # 闭包函数外的函数中
#     def inner():
#         i_count = 2  # 局部作用域

#
# Python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，
# 其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，
# 也就是说这这些语句内定义的变量，外部也可以访问
# if True:
#     msg = 'if语句块定义信息msg'
#
# print(msg)  # msg是定义在if语句块中的,但是外部还是可以访问的

# 执行结果:
# if语句块定义信息msg

#
# def test():
#     msg_inner = '定义在函数内部的msg_inner'
#
# print(msg_inner)  # 错误
#
# # 执行结果
# # Traceback (most recent call last):
# #   File "/Users/hkkhuang/Documents/Python/PythonBasic/009_function.py", line 304, in <module>
# #     print(msg_inner)
# # NameError: name 'msg_inner' is not defined



# 14----------------------------------
# # 局部变量和全局变量
# total = 0  # 定义一个全局变量total
# print('函数外的是全局变量:', total)
#
# def printInfo():
#     print('访问全局变量:', total)
#
#
# def sum(arg1, arg2):
#     # print(total)
#     total = arg1 + arg2
#     print('函数内部的total是局部变量:', total)
#     return total
#
# printInfo()
# total = sum(1, 2)
#
# print('接收返回的total:', total)
# # 执行结果:
# # 函数外的是全局变量: 0
# # 函数内部的是局部变量: 3
# # 接收返回的total: 3


# num = 1
#
# def fun1():
#     print(num)
#
# fun1()
#
# # 输出结果:
# # 1


# 15----------------------------------
# # global 和 nonlocal关键字
# # 当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。
# num = 1
# def test():
#     global num  # 使用golbal关键字声明
#     print(num)
#     num = 321
#     print(num)
#
#
# test()
#
# # # 执行结果
# # 1
# # 321




# ----------------------------------
#
# num = 1
#
# def test():
#     global num  # 使用golbal关键字声明
#     print('函数内输出全局变量:', num)
#     num = 321
#     print('函数内部使用global关键字修改后的全局变量:', num)
#
# print('外部输出全局变量', num)
#
# test()

# 执行结果
# 外部输出全局变量 1
# 函数内输出全局变量: 1
# 函数内部使用global关键字修改后的全局变量: 321


# 16----------------------------------
# 如果要修改嵌套作用域（enclosing 作用域，外层非全局作用域）中的变量则需要 nonlocal 关键字
# def outer():
#     num = 10
#     def inner():
#         nonlocal num   # nonlocal关键字声明
#         num = 100
#         print(num)
#     inner()
#     print(num)
#
#
# outer()
#
# # 执行结果:
# # 100
# # 100

# --------------------------------------
# for i in range(10):
#     age = i
#     print(age)
#
# print(age)
#
# # 执行结果:
# # 0
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
# # 9