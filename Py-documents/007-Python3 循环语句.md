# 007-Python3 循环语句

Python中的循环语句有 for 和 while。

##  while 循环

Python中while语句的一般形式：
	
	while 判断条件：
	    语句

同样需要**注意冒号和缩进**。另外，在Python中**没有do..while**循环。 

	
	n = 100
	sumTotal = 0
	counter = 1
	while counter <= n:
	    sumTotal += counter
	    counter += 1
	
	print('1+2+...+100=',sumTotal)
	
	# 执行结果:
	1+2+...+100= 5050
	
无限循环

我们可以通过设置条件表达式永远不为 false 来实现无限循环.

#### 实例

	var = 1
	while var == 1 :  # 表达式永远为 true
	   num = int(input("输入一个数字  :"))
	   print ("你输入的数字是: ", num)
	 
	print ("Good bye!")
	

## while 循环使用 else 语句

在 while … else 在条件语句为 false 时执行 else 的语句块：
	
	count = 0
	while count < 5:
	    print(count, " 小于 5")
	    count = count + 1
	else:
	    print(count, " 大于或等于 5")
	    
	执行条件:
	0  小于 5
	1  小于 5
	2  小于 5
	3  小于 5
	4  小于 5
	5  大于或等于 5
	
##  简单语句组

类似if语句的语法，如果你的while循环体中只有一条语句，你可以将该语句与while写在同一行中.

**实例**
		 
	flag = 1
	 
	while (flag): print ('hello 这是简单语句!')
	 
	print ("Good bye!")

**注意：**以上的无限循环你可以使用 CTRL+C 来中断循环。

## for 语句

Python for循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：

	for <variable> in <sequence>:
	    <statements>
	else:
	    <statements>
	    
**实例:**

	
	languages = ['C', 'C++', 'Java', 'Python']
	for x in languages:
	    print(x)
	    
	执行结果:
	C
	C++
	Java
	Python
	
以下 for 实例中使用了 break 语句，break 语句用于跳出当前循环体：

**实例**
	 
	
	sites = ["Baidu", "Google", "YZU", "Taobao"]
	for site in sites:
	    if site == "YZU":
	        print("扬州大学!")
	        break
	    print("循环数据 " + site)
	else:
	    print("没有循环数据!")
	print("完成循环!")
	
	# 执行结果:
	循环数据 Baidu
	循环数据 Google
	循环数据 yzu.com
	循环数据 Taobao
	没有循环数据!
	完成循环!
	
##  range()函数

如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列.
	
	for i in range(5):
	    print(i)
	    
	执行结果:
	0
	1
	2
	3
	4

也可以使用range指定区间的值：
	
	for i in range(5,9):
	    print(i)
	    
	执行结果:
	5
	6
	7
	8

也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'): 
	
	for i in range(0, 10, 3):
	    print(i)
	
	执行结果:
	0
	3
	6
	9
	
负数:

	for i in range(-10, -100, -30):
	    print(i)
	
	# 执行结果:
	-10
	-40
	-70
	
可以结合range()和len()函数以遍历一个序列的索引:

	a = ['Google', 'Baidu', 'YZU', 'Taobao', 'QQ']
	for i in range(len(a)):
	    print(i, a[i])
	
	# 执行结果:
	0 Google
	1 Baidu
	2 YZU
	3 Taobao
	4 QQ
	
还可以使用range()函数来创建一个列表:
		
	a = list(range(5))
	print(a)
	
	# 执行结果:
	[0, 1, 2, 3, 4]

 break和continue语句及循环中的else子句

break 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

	
	for letter in 'Huangkeke':  # 第一个实例
	    if letter == 'g':
	        break
	    print('当前字母为 :', letter)
	
	var = 10  # 第二个实例
	while var > 0:
	    print('当期变量值为 :', var)
	    var = var - 1
	    if var == 5:
	        break
	
	print("Good bye!")
	
	# 执行结果:
	当前字母为 : H
	当前字母为 : u
	当前字母为 : a
	当前字母为 : n
	当期变量值为 : 10
	当期变量值为 : 9
	当期变量值为 : 8
	当期变量值为 : 7
	当期变量值为 : 6
	Good bye!
	
continue语句被用来告诉Python跳过当前循环块中的剩余语句，然后继续进行下一轮循环。
	
	
	for letter in 'Huangkeke':  # 第一个实例
	    if letter == 'o':  # 字母为 o 时跳过输出
	        continue
	    print('当前字母 :', letter)
	
	var = 10  # 第二个实例
	while var > 0:
	    var = var - 1
	    if var == 5:  # 变量为 5 时跳过输出
	        continue
	    print('当前变量值 :', var)
	print("Good bye!")
	
	# 执行结果:
	当前字母 : H
	当前字母 : u
	当前字母 : a
	当前字母 : n
	当前字母 : g
	当前字母 : k
	当前字母 : e
	当前字母 : k
	当前字母 : e
	当前变量值 : 9
	当前变量值 : 8
	当前变量值 : 7
	当前变量值 : 6
	当前变量值 : 4
	当前变量值 : 3
	当前变量值 : 2
	当前变量值 : 1
	当前变量值 : 0
	Good bye!
	
循环语句可以有 else 子句，它在穷尽列表(以for循环)或条件变为 false (以while循环)导致循环终止时被执行,但循环被break终止时不执行。

查询质数的循环例子:

	
	for n in range(2, 10):
	    for x in range(2, n):
	        if n % x == 0:
	            print(n, '等于', x, '*', n//x)
	            break
	    else:
	        # 循环中没有找到元素
	        print(n, ' 是质数')
	
	# 执行结果:
	2  是质数
	3  是质数
	4 等于 2 * 2
	5  是质数
	6 等于 2 * 3
	7  是质数
	8 等于 2 * 4
	9 等于 3 * 3

## pass 语句

Python pass是空语句，是为了保持程序结构的完整性。

pass 不做任何事情，一般用做占位语句
	
	while True:
	...     pass  # 等待键盘中断 (Ctrl+C)
	
实例:

	
	for letter in 'Huangkeke':
	    if letter == 'g':
	        pass
	        print('执行 pass 块')
	    print('当前字母 :', letter)
	
	print("Good bye!")
	
	执行结果:
	当前字母 : H
	当前字母 : u
	当前字母 : a
	当前字母 : n
	执行 pass 块
	当前字母 : g
	当前字母 : k
	当前字母 : e
	当前字母 : k
	当前字母 : e
	Good bye!
