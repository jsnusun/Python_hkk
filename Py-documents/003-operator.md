# Python3-运算符
Python3主要支持一下运算符：

* 算数运算符
* 比较（关系）运算符
* 赋值运算符
* 逻辑运算符
* 位运算符
* 成员运算符
* 身份运算符
* 运算符优先级

## python算数运算符

	运算符		描述							             
	+		  加法-两个对象相加
	-		  减法-得到负数或者一个数减去一个数
	*		  乘法-两个数相乘或者返回一个被重复若干次的字符串
	/		  除法-x除以y
	% 		  取模-返回除法的余数
	**		  幂-返回x的y次幂
	//		  取整除-返回商的整数部分
	
实例：

	#!/usr/bin/python3

	a = 21
	b = 10
	c = 0
	
	c = a + b
	print("1 - c 的值为：", c)
	
	c = a - b
	print("2 - c 的值为：", c)
	
	c = a * b
	print("3 - c 的值为：", c)
	
	c = a / b
	print("4 - c 的值为：", c)
	
	c = a % b
	print("5 - c 的值为：", c)
	
	# 修改变量 a 、b 、c
	a = 2
	b = 3
	c = a ** b
	print("6 - c 的值为：", c)
	
	a = 10
	b = 5
	c = a // b
	print("7 - c 的值为：", c)
	
	# 执行结果
	1 - c 的值为： 31
	2 - c 的值为： 11
	3 - c 的值为： 210
	4 - c 的值为： 2.1
	5 - c 的值为： 1
	6 - c 的值为： 8
	7 - c 的值为： 2
	
## Python比较运算符

	假设变量 a=1,b=2
	运算符			描述					          实例
	==			  等于-比较对象是否相等             (a==b)  False
	!=			  不等于-比较两个对象是否不相等      (a!=b)  Ture
	>			  大于-返回x是否大于y              (a>b)   False
	<			  小于-返回x是否小于y              (a<b)   True
	>=			  大于等于                        (a>=b)  False
	<=			  小于等于                        (a<=b)  True
	
实例：

	# python比较运算符
	a = 1
	b = 2
	c = 0
	
	if (a == b):
	    print("1 - a 等于 b")
	else:
	    print("1 - a 不等于 b")
	
	if (a != b):
	    print("2 - a 不等于 b")
	else:
	    print("2 - a 等于 b")
	
	if (a < b):
	    print("3 - a 小于 b")
	else:
	    print("3 - a 大于等于 b")
	
	if (a > b):
	    print("4 - a 大于 b")
	else:
	    print("4 - a 小于等于 b")
	
	# 修改变量 a 和 b 的值
	a = 10;
	b = 20;
	if (a <= b):
	    print("5 - a 小于等于 b")
	else:
	    print("5 - a 大于  b")
	
	if (b >= a):
	    print("6 - b 大于等于 a")
	else:
	    print("6 - b 小于 a")
	
	# 运行结果
	1 - a 不等于 b
	2 - a 不等于 b
	3 - a 小于 b
	4 - a 小于等于 b
	5 - a 小于等于 b
	6 - b 大于等于 a

	
## Python赋值运算符

	运算符               描述
	=                   简单的赋值运算符
	+=                  加法赋值运算符
	-=                  减法赋值运算符
	*=                  乘法赋值运算符
	/=                  除法赋值运算符
	%=                  取模赋值运算符
	**=                 幂赋值运算符
	//=                 取整除赋值运算符
	
实例：

	# Python赋值运算符
	a = 21
	b = 10
	c = 0
	
	c = a + b
	print("1 - c 的值为：", c)
	
	c += a
	print("2 - c 的值为：", c)
	
	c *= a
	print("3 - c 的值为：", c)
	
	c /= a
	print("4 - c 的值为：", c)
	
	c = 2
	c %= a
	print("5 - c 的值为：", c)
	
	c **= a
	print("6 - c 的值为：", c)
	
	c //= a
	print("7 - c 的值为：", c)
	
	# 执行结果：
	1 - c 的值为： 31
	2 - c 的值为： 52
	3 - c 的值为： 1092
	4 - c 的值为： 52.0
	5 - c 的值为： 2
	6 - c 的值为： 2097152
	7 - c 的值为： 99864
		
## Python位运算符

按位运算符就是把数字看做是二进制进行计算。

	运算符  描述	                                                                         
	&	   按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0                  
	|	   按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。                             
	^	   按位异或运算符：当两对应的二进位相异时，结果为1                                        
	~	   按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1             
	<<	   左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0  
	>>	   右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数         
	
	
实例：

	# Python 位运算符
	a = 60  # 60 = 0011 1100
	b = 13  # 13 = 0000 1101
	c = 0
	
	c = a & b;  # 12 = 0000 1100
	print("1 - c 的值为：", c)
	
	c = a | b;  # 61 = 0011 1101
	print("2 - c 的值为：", c)
	
	c = a ^ b;  # 49 = 0011 0001
	print("3 - c 的值为：", c)
	
	c = ~a;  # -61 = 1100 0011
	print("4 - c 的值为：", c)
	
	c = a << 2;  # 240 = 1111 0000
	print("5 - c 的值为：", c)
	
	c = a >> 2;  # 15 = 0000 1111
	print("6 - c 的值为：", c)
	
	# 执行结果
	1 - c 的值为： 12
	2 - c 的值为： 61
	3 - c 的值为： 49
	4 - c 的值为： -61
	5 - c 的值为： 240
	6 - c 的值为： 15
	
## Python逻辑运算符

	运算符	     逻辑表达式    描述	
	and        x and y	   布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。 
	or         x or y	   布尔"或" - 如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
	not	       not x	   布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
	
	python 中的 and 从左到右计算表达式，若所有值均为真，则返回最后一个值，若存在假，返回第一个假值；
	or 也是从左到有计算表达式，返回第一个为真的值；
	其中数字 0 是假，其他都是真；
	
实例：

	# Python逻辑运算符
	a = 10
	b = 20
	
	if (a and b):
	    print("1 - 变量 a 和 b 都为 true")
	else:
	    print("1 - 变量 a 和 b 有一个不为 true")
	
	if (a or b):
	    print("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
	else:
	    print("2 - 变量 a 和 b 都不为 true")
	
	# 修改变量 a 的值
	a = 0
	if (a and b):
	    print("3 - 变量 a 和 b 都为 true")
	else:
	    print("3 - 变量 a 和 b 有一个不为 true")
	
	if (a or b):
	    print("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
	else:
	    print("4 - 变量 a 和 b 都不为 true")
	
	if not (a and b):
	    print("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
	else:
	    print("5 - 变量 a 和 b 都为 true")
	    
	# 执行结果
	1 - 变量 a 和 b 都为 true
	2 - 变量 a 和 b 都为 true，或其中一个变量为 true
	3 - 变量 a 和 b 有一个不为 true
	4 - 变量 a 和 b 都为 true，或其中一个变量为 true
	5 - 变量 a 和 b 都为 false，或其中一个变量为 false
	

## Python成员运算符
	运算符     描述                                               实例
	in	      如果在指定的序列中找到值返回 True，否则返回 False。      x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
	not in	  如果在指定的序列中没有找到值返回 True，否则返回 False。   x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

实例：

	# python 成员运算符
	a = 10
	b = 20
	myList = [1, 2, 3, 4, 5];
	
	if (a in myList):
	    print("1 - 变量 a 在给定的列表中 list 中")
	else:
	    print("1 - 变量 a 不在给定的列表中 list 中")
	
	if (b not in myList):
	    print("2 - 变量 b 不在给定的列表中 list 中")
	else:
	    print("2 - 变量 b 在给定的列表中 list 中")
	
	# 修改变量 a 的值
	a = 2
	if (a in myList):
	    print("3 - 变量 a 在给定的列表中 list 中")
	else:
	    print("3 - 变量 a 不在给定的列表中 list 中")
	    
	# 执行结果
	1 - 变量 a 不在给定的列表中 list 中
	2 - 变量 b 不在给定的列表中 list 中
	3 - 变量 a 在给定的列表中 list 中
	
## python身份运算符
身份运算符用于比较两个对象的存储单元。

	运算符   描述	                                     实例
	is      is 是判断两个标识符是不是引用自一个对象         x is y, 类似 id(x) == id(y) , 如果引用的是同一个对象则返回 True，否则返回 False
	is not  is not 是判断两个标识符是不是引用自不同对象     x is not y ， 类似 id(a) != id(b)。如果引用的不是同一个对象则返回结果 True，否则返回 False。
	
实例：

	# python身份运算符
	a = 20
	b = 20
	
	if (a is b):
	    print("1 - a 和 b 有相同的标识")
	else:
	    print("1 - a 和 b 没有相同的标识")
	
	if (id(a) == id(b)):
	    print("2 - a 和 b 有相同的标识")
	else:
	    print("2 - a 和 b 没有相同的标识")
	
	# 修改变量 b 的值
	b = 30
	if (a is b):
	    print("3 - a 和 b 有相同的标识")
	else:
	    print("3 - a 和 b 没有相同的标识")
	
	if (a is not b):
	    print("4 - a 和 b 没有相同的标识")
	else:
	    print("4 - a 和 b 有相同的标识")
	    
	# 执行结果：
	1 - a 和 b 有相同的标识
	2 - a 和 b 有相同的标识
	3 - a 和 b 没有相同的标识
	4 - a 和 b 没有相同的标识
	
注意：

	is和 == 区别
	is 是用于判断两个变量引用对象是否是同一个
	== 是用于判断引用变量的值是否相等
	
	a = [1, 2, 3]
	b = a
	print(b)
	print(b is a)
	print(b == a)
	b = a[:]
	print(b)
	print(b is a)
	print(b == a)
	# 执行结果
	[1, 2, 3]
	True
	True
	[1, 2, 3]
	False
	True
	
## Python优先级

	运算符						描述（优先等级由高到低）
	**						指数（最高优先级）
	~ + -					按位取反，一元加，减（后两个方法名是+@ 和 -@）
	* / % //				乘，除，取模，取整
	+ - 					加法，减法
	<<  >>					左移，右移
	&						位 ‘AND’
	^ |						位运算符
	< > <= >=				比较运算符
	== !=					等于运算符
	= %=  /= //= += -= *=   赋值运算符
	is  is not 				身份运算符
	in  not in				成员运算符
	not or and				逻辑运算符
	
实例：

	# 运算符优先级
	a = 20
	b = 10
	c = 15
	d = 5
	e = 0
	
	e = (a + b) * c / d  # ( 30 * 15 ) / 5
	print("(a + b) * c / d 运算结果为：", e)
	
	e = ((a + b) * c) / d  # (30 * 15 ) / 5
	print("((a + b) * c) / d 运算结果为：", e)
	
	e = (a + b) * (c / d);  # (30) * (15/5)
	print("(a + b) * (c / d) 运算结果为：", e)
	
	e = a + (b * c) / d;  # 20 + (150/5)
	print("a + (b * c) / d 运算结果为：", e)
	
	执行结果：
	(a + b) * c / d 运算结果为： 90.0
	((a + b) * c) / d 运算结果为： 90.0
	(a + b) * (c / d) 运算结果为： 90.0
	a + (b * c) / d 运算结果为： 50.0
		









	
	