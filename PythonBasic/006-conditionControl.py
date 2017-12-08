#!/usr/bin/python3

# var1 = 100
# if var1:
#     print('1-if表达式条件为true')
#     print(var1)
#
# var2 = 0
# if var2:
#     print('2-if表达式条件为true')
#     print(var2)
# else:
#     print('2-if表达式条件为false')
#     print(var2)
#
# print('结束,bye!')
#
# # 执行结果
# 1-if表达式条件为true
# 100
# 2-if表达式条件为false
# 0
# 结束,bye!

# # 判断狗的年龄
# age = int(input('输入狗狗的年龄:'))
# print('')
# if age < 0:
#     print('请不要逗比')
# elif age == 1:
#     print('1岁的狗狗相当于14岁的人')
# elif age == 2:
#     print('2岁的狗狗相当于22岁的人')
# elif age > 2:
#     human = 22 + (age - 2)*5
#     print('%d岁的狗狗相当于%d岁的人' % (age, human))
#
# print('')
# input('按下enter键结束')
#
# # 演示 == 操作符
#
# # 使用数字
# print(2 == 3)
#
# # 使用变量
# x = 4
# y = 5
# print(x == y)
#
# # 执行结果
# False
# False

# # 演示数字的比较运算
#
# play = True
#
# while play:
#     number = 10
#     guess = -1
#     count = 0
#     print('---数字猜猜猜---')
#     while (guess != number) & (count < 5):
#         guess = int(input('输入你想猜的数字:'))
#
#         if guess == number:
#             count += 1
#             print('哇哦,猜对了')
#             print('猜了%d次' % (count,))
#         elif guess > number:
#             print('啊偶,猜大了...')
#             count += 1
#             print('猜了%d次' % (count,))
#         elif guess < number:
#             print('哈哈,猜小了...')
#             count += 1
#             print('猜了%d次' % (count,))
#
#     if count == 5:
#         print('最多猜5次哦,下次再来玩吧')
#         playAgain = int(input('还要再玩一次吗?继续,输入 1,结束输入 0:'))
#         if playAgain == 1:
#             play = True
#         elif playAgain == 0:
#             play = False
#         else:
#             print('输入错误')
#             play = False


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

