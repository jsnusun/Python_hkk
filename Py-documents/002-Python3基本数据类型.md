# Python3基本数据类型
---
Python 中的变量**不需要声明**。每个变量在**使用前都必须赋值**，变量**赋值以后**该变量才会**被创建**。
在 Python 中，**变量就是变量，它没有类型**，我们所说的"类型"是变量所指的内存中对象的类型。
等号（=）用来给变量赋值。
等号（=）运算符左边是一个变量名,等号（=）运算符右边是存储在变量中的值。例如：

	#!/usr/bin/python3
 
	counter = 100          # 整型变量
	miles   = 1000.0       # 浮点型变量
	name    = "hkkhuang"     # 字符串
	 
	print (counter)
	print (miles)
	print (name)
	
## 多个变量赋值
Python允许你同时为多个变量赋值。例如：

	a, b, c = 1, 2, "huangkeke"
	上面语句创建两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "huangkeke" 分配给变量 c。
	
	
## 标准数据类型

Python3 中有六个标准的数据类型：

* Number（数字）
* String（字符串）
* List（列表）
* Tuple（元组）
* Sets（集合）
* Dictionary（字典)

## Number(数字)
Python3 支持 **int、float、bool、complex（复数）**。**python3只有一种整数类型 int，表示为长整型**，没有 python2 中的 Long。像大多数语言一样，数值类型的赋值和计算都是很直观的。内置的 **type() 函数**可以用来查询变量所指的对象类型。

	a, b, c, d = 20, 5.5, True, 4+3j
	print(type(a), type(b), type(c), type(d))
	
	运行结果：
	<class 'int'> <class 'float'> <class 'bool'> <class 'complex'>
	
还可以用 isinstance 来判断：

	a = 123
	print(isinstance(a, int))	
	运行结果：True
	
isinstance 和 type 的区别在于：	
type()不会认为子类是一种父类类型。
isinstance()会认为子类是一种父类类型。

	class A:
	    pass
	
	
	class B(A):
	    pass
	
	
	print(isinstance(A(), A))  # returns True
	print(type(A()) == A)      # returns True
	print(isinstance(B(), A))    # returns True
	print(type(B()) == A)        # returns False
	
	注意：在 Python2 中是没有布尔型的，它用数字 0 表示 False，用 1 表示 True。到
	Python3 中，把 True 和 False 定义成关键字了，但它们的值还是 1 和 0，它们可以和数字相加。
	
## 数值运算

	print(5+4)     # 加法
	print(4.6-4)   # 减法
	print(3*5)     # 乘法
	print(9/3)     # 除法，得到一个浮点数
	print(2//4)    # 除法  得到一个整数
	print(19%3)    # 取余
	print(2**5)    # 乘方
	
	运算结果：
	9
	0.5999999999999996
	15
	3.0
	0
	1
	32
	
	注意：
	1、Python可以同时为多个变量赋值，如a, b = 1, 2。
	2、一个变量可以通过赋值指向不同类型的对象。
	3、数值的除法（/）总是返回一个浮点数，要获取整数使用//操作符。
	4、在混合计算时，Python会把整型转换成为浮点数。
	
	Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型
	
## String字符串

Python中的字符串用单引号(')或双引号(")括起来，同时使用反斜杠(\)转义特殊字符。
字符串的截取的语法格式如下：

	变量[头下标:尾下标]

索引值以 0 为开始值，-1 为从末尾的开始位置。

加号 (+) 是字符串的连接符， 星号 (*) 表示复制当前字符串，紧跟的数字为复制的次数。

	myStr = 'ILovePython'
	
	print(myStr)  # 输出字符串
	print(myStr[0:-1])  # 输出第一个到倒数第二个的所有字符
	print(myStr[0])  # 输出字符串第一个字符
	print(myStr[2:5])  # 输出从第三个开始到第五个的字符
	print(myStr[2:])  # 输出从第三个开始的后的所有字符
	print(myStr * 2)  # 输出字符串两次
	print(myStr + "TEST")  # 连接字符串
	
	运行结果：
	ILovePython
	ILovePytho
	I
	ove
	ovePython
	ILovePythonILovePython
	ILovePythonTEST

Python 使用**反斜杠(\)**转义特殊字符，如果你不想让反斜杠发生转义，可以在**字符串前面添加一个 R 或者 r**，表示原始字符串：

	# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串：
	print('my name is huangkeke')     # 输出字符串
	print("My name is \nhuangkeke")   # 转义字符 \n 表示换行
	print(r"my name is \nhuangkeke")  # 在字符串前面加上r 或者 R 表示原样输出字符串
	
	# 运行结果
	my name is huangkeke
	My name is 
	huangkeke
	my name is \nhuangkeke
	
反斜杠(\)可以作为续行符，表示下一行是上一行的延续。也可以使用 """...""" 或者 '''...''' 跨越多行。
注意，Python 没有单独的字符类型，一个字符就是长度为1的字符串。

	print('Hi,nice to meet you\
	my name \
	is huangkeke')
	
	print('''Hi,nice to meet you'''
	'''my name '''
	'''is huangkeke''')