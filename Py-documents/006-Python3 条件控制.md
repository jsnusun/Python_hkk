# 006-Python3 条件控制

Python条件语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

if 语句

Python中if语句的一般形式如下所示：

	if condition_1:
	    statement_block_1
	elif condition_2:
	    statement_block_2
	else:
	    statement_block_3
	    
    如果 "condition_1" 为 True 将执行 "statement_block_1" 块语句
    如果 "condition_1" 为False，将判断 "condition_2"
    如果"condition_2" 为 True 将执行 "statement_block_2" 块语句
    如果 "condition_2" 为False，将执行"statement_block_3"块语句

**注意:Python 中用 elif 代替了 else if，所以if语句的关键字为：if – elif – else。**

**注意：**

1、每个条件后面要使用**冒号（:）**，表示接下来是满足条件后要执行的语句块。

2、使用**缩进**来划分语句块，相同缩进数的语句在一起组成一个语句块。

3、在Python中**没有switch – case语句**。

#### 实例:
	
	#!/usr/bin/python3
	
	var1 = 100
	if var1:
	    print('1-if表达式条件为true')
	    print(var1)
	
	var2 = 0
	if var2:
	    print('2-if表达式条件为true')
	    print(var2)
	else:
	    print('2-if表达式条件为false')
	    print(var2)
	
	print('结束,bye!')
	
	# 执行结果
	1-if表达式条件为true
	100
	2-if表达式条件为false
	0
	结束,bye!
	
#### 实例
	
	# 判断狗的年龄
	age = int(input('输入狗狗的年龄:'))
	print('')
	if age < 0:
	    print('请不要逗比')
	elif age == 1:
	    print('1岁的狗狗相当于14岁的人')
	elif age == 2:
	    print('2岁的狗狗相当于22岁的人')
	elif age > 2:
	    human = 22 + (age - 2)*5
	    print('%d岁的狗狗相当于%d岁的人' % (age, human))
	
	print('')
	input('按下enter键结束')
	
### if中常用的操作运算符
	操作符      说明
	<          小于
	<=         小于等于
	>          大于
	>=         大于等于
	==         等于,用于比较对象是否相等
	!=         不等于
	
#### 实例:
	
	# 演示 == 操作符
	
	# 使用数字
	print(2 == 3)
	
	# 使用变量
	x = 4
	y = 5
	print(x == y)
	
	# 执行结果
	False
	False
	
#### 实例:

	# 演示数字的比较运算	

	play = True
	
	while play:
	    number = 10
	    guess = -1
	    count = 0
	    print('---数字猜猜猜---')
	    while (guess != number) & (count < 5):
	        guess = int(input('输入你想猜的数字:'))
	
	        if guess == number:
	            count += 1
	            print('哇哦,猜对了')
	            print('猜了%d次' % (count,))
	        elif guess > number:
	            print('啊偶,猜大了...')
	            count += 1
	            print('猜了%d次' % (count,))
	        elif guess < number:
	            print('哈哈,猜小了...')
	            count += 1
	            print('猜了%d次' % (count,))
	
	    if count == 5:
	        print('最多猜5次哦,下次再来玩吧')
	        playAgain = int(input('还要再玩一次吗?继续,输入 1,结束输入 0:'))
	        if playAgain == 1:
	            play = True
	        elif playAgain == 0:
	            play = False
	        else:
	            print('输入错误')
	            play = False


## if 嵌套

在嵌套 if 语句中，可以把 if...elif...else 结构放在另外一个 if...elif...else 结构中。
	
	if 表达式1:
	    语句
	    if 表达式2:
	        语句
	    elif 表达式3:
	        语句
	    else:
	        语句
	elif 表达式4:
	    语句
	else:
	    语句

#### 实例:
	
	num = int(input("输入一个数字："))
	if num % 2 == 0:
	    if num % 3 == 0:
	        print("你输入的数字可以整除 2 和 3")
	    else:
	        print("你输入的数字可以整除 2，但不能整除 3")
	else:
	    if num % 3 == 0:
	        print("你输入的数字可以整除 3，但不能整除 2")
	    else:
	        print("你输入的数字不能整除 2 和 3")