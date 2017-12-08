# 008-Python3 迭代器与生成器
## 迭代

如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。

在Python中，迭代是通过**for ... in**来完成的，而很多语言比如C或者Java，迭代list是通过下标完成的.

比如Java代码：

	for (i=0; i<list.length; i++) {
	    n = list[i];
	}

可以看出，Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

	d = {'a': 1, 'b': 2, 'c': 3}
	for key in d:
		print(key)
		
	# 执行结果
	a
	c
	b

**因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。**

**[LOOK LOOK]**

	默认情况下，dict迭代的是key。
	
	如果要迭代value，可以用for value in d.values()
	
	如果要同时迭代key和value，可以用for k, v in d.items()。
	
		
	d = {'a': 1, 'b': 2, 'c': 3}
	for key in d:
	    print(key)
	    
	print('----------------')
	for value in d.values():
	    print(value)
	
	print('-----------------')
	for k, v in d.items():
	    print(k, end=':')
	    print(v)
	
	# 执行过程:
	a
	b
	c
	----------------
	1
	2
	3
	-----------------
	a:1
	b:2
	c:3

由于字符串也是可迭代对象，因此，也可以作用于for循环：

	 字符串循环迭代
	str = 'YZUHKK'
	for s in str:
	    print(s)
	    
	# 执行结果:
	Y
	Z
	U
	H
	K
	K

所以，当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：

	from collections import Iterable
	print(isinstance('1234', Iterable))
	print(isinstance([1,2,3], Iterable))
	print(isinstance(123, Iterable))
	
	# 执行结果
	True
	True
	False

**字符串，列表或元组对象**都可用于创建迭代器：
	
	myList = [1, 2, 3, 4, 5]
	it = iter(myList)
	print(next(it))  #从0开始 读取下一个位置 1
	
	print(next(it))  #从0开始 读取下一个位置 2

最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的**enumerate函数**可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：


	for i, value in enumerate(['A','B','YZU']):
	    print(i,value)
	
	# 执行结果:
	0 A
	1 B
	2 YZU

## 列表生成器
列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：

	myList = list(range(1,20))
	print(myList)
	
	# 执行结果:[不包括上限]
	[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
	
生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？

方法一是循环：
	
	myList = []
	for x in range(1, 11):
	    myList.append(x * x)
	 
	print(myList)
	
	# 执行结果:
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

但是循环太过于繁琐,使用列表生成器则可以使用一行语句代替循环生成的list
	
	myList = [x * x for x in range(1, 11)]
	print(myList)
	
	执行结果:\
	[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
	
写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。

for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：

	
	myList = [x * x for x in range(1, 11) if x % 2 == 0]
	print(myList)
	
	执行结果:
	[4, 16, 36, 64, 100]
	
还可以使用两层循环，可以生成全排列：

	
	# 还可以使用两层循环，可以生成全排列：
	myList = [m + n for m in 'JSNU' for n in 'YZU']
	print(myList)
	
	# 执行结果
	['JY', 'JZ', 'JU', 'SY', 'SZ', 'SU', 'NY', 'NZ', 'NU', 'UY', 'UZ', 'UU']

运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

	import os
	myDir = [d for d in os.listdir('.')]
	print(myDir)
	
	# 执行结果:
	['008-iterator.py', '006-conditionControl.py', '007-loopStructure.py', '005-String.py', '004-python_Number.py', '003_operator.py', '.idea']
	
如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：
	
	>>> L = ['Hello', 'World', 18, 'Apple', None]
	>>> [s.lower() for s in L]
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "<stdin>", line 1, in <listcomp>
	AttributeError: 'int' object has no attribute 'lower'
	
使用内建的isinstance函数可以判断一个变量是不是字符串：

	L1 = ['Hello', 'World', 18, 'Apple', None]
	L2 = []
	for s in L1:
	    if isinstance(s, str):
	        L2.append(s.lower())
	
	print('转换结束')
	print(L2)

## 生成器

通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：

	
	# 生成器
	g = (x * x for x in range(10))
	print(g)
	
	# 执行结果:
	<generator object <genexpr> at 0x104a7c888>

创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator。

我们可以直接打印出list的每一个元素，但我们怎么打印出generator的每一个元素呢？

如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：

	
	# 生成器
	g = (x * x for x in range(10))
	print(g)
	
	# 执行结果:
	# <generator object <genexpr> at 0x104a7c888>
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	print(next(g))
	
	# 执行结果
	# 0
	# 1
	# 4
	# 9
	# 16
	# 25
	# 36
	# 49
	# 64
	# 81
	
	print(next(g))  # generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
	
	# Traceback (most recent call last):
	#   File "/Users/hkkhuang/Documents/Python/PythonBasic/008-iterator.py", line 187, in <module>
	#     print(next(g))
	# StopIteration
	# <generator object <genexpr> at 0x103a7c888>
	# 0
	# 1
	# 4
	# 9
	# 16
	# 25
	# 36
	# 49
	# 64
	# 81


generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

当然，上面这种不断调用next(g)实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：
	
	
	g = (x * x for x in range(10))
	
	for x in g:
	    print(x)
	    
	# 执行结果
	0
	1
	4
	9
	16
	25
	36
	49
	64
	81

所以，我们创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，并且不需要关心StopIteration的错误。

generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。

比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：

1, 1, 2, 3, 5, 8, 13, 21, 34, ...

斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：

	
	# 函数实现Fibonacci数列
	
	def fib(mymax):
	    n, a, b = 0, 0, 1
	    while n < mymax:
	        print(b,end=' ')
	        a, b = b, a+b
	        n = n + 1
	    return 'done'
	
	fib(20)
	
	# 执行结果:
	1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
	
仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
	
	
	# # 函数实现Fibonacci数列
	# 函数改为generator 生成器
	
	def fib(max):
	    n, a, b = 0, 0, 1
	    while n < max:
	        yield b
	        a, b = b, a+b
	        n = n + 1
	    return 'done'
	
	
	f = fib(20)
	
	print(type(f))  # 判断类型为<class 'generator'>
	
	for x in f:
	    print(x, end=' ')
	
	# 执行结果:
	<class 'generator'>
	1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 done

这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator.

这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


## 迭代器

我们已经知道，可以直接作用于for循环的数据类型有以下几种：

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

可以使用isinstance()判断一个对象是否是Iterable对象：


迭代是Python最强大的功能之一，是**访问集合元素**的一种方式。。

**迭代器是一个可以记住遍历的位置的对象**。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器**只能往前不会后退**。

迭代器有两个基本的方法：**iter() 和 next()。**



---
	
迭代器对象可以使用常规for语句进行遍历:

	
	myList = [1, 2, 3, 4, 5]
	it = iter(myList)  #创建迭代器对象
	for x in it:
	    print(x)  #从0开始 读取下一个位置 1
	
	# 执行结果:
	1
	2
	3
	4
	5
	----------------------------------------------
		
	myList = [1, 2, 3, 4, 5]
	it = iter(myList)  #创建迭代器对象
	for x in it:
	    print(x, end=(" "))  #从0开始 读取下一个位置 1
	
	# 执行结果:
	1 2 3 4 5 
	
