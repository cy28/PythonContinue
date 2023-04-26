"""
while循环结构的语法：

初始条件
while 判断条件：
    循环体
    更新条件

注意：
1 在while循环中，初始条件只会在第一次循环中执行
2 在python中，没有自增自减运算符
3 在python中，没有do while循环结构

"""

# 1. 练习一：打印1-50之间能被3整除的数字

# num = 0
# while num < 50:
#     num += 1
#     if num % 3 == 0:
#         print(num)


# 2. 练习二： 打印1-10之间数字的累加和

# sum_target = 0
# num1 = 0
# target = int(input('请输入你要计算的累加和：'))
#
# while num1 < target:
#     num1 += 1
#     sum_target += num1
# print(sum_target)


"""

for循环结构语法：

    for i in 可迭代对象
执行过程: 
1. 先生成对象序列
2. 然后将对象中的值依次赋给i
        
注意：
1. python中的可迭代对象一般指的是字符串、列表，元祖，集合等
2. range(start(包含), stop(不包含), step(步长,默认为1))是用来生成指定区间的整数序列
   第一个参数表示从几开始，包含这个数
   第二个参数表示到几结束，不包含这个数

"""


# 练习一: 1-50的累加和

# sum1 = 0
# for i in range(1, 51):
#     sum1 += i
# print(sum1)


# 练习二: 输入用户名和密码,如果三次没有登录成功,则提示账号被锁定

for i in range(3):
    username = input('请输入你的用户名:')
    password = input('请输入你的密码:')
    if username == 'admin' and password == '1234':
        print('登录成功!')
        break
    print('用户名或密码输入错误!')
else:
    if i == 2:
        print('账户被锁定!')


"""
for else 语法:

for i in range(n):
    循环体
else:
    如果上面的for循环, 循环了0-n-1次,没有出现中断
----------------------------------------------------------------------------------------------------------------------
在Python中，for else语句的使用方式是：

for item in sequence:
    if condition:
        # some code to execute
        break
else:
    # some code to execute if the loop completes without hitting a "break" statement
    
在这个结构中，for循环遍历一个序列（如列表、元组、字符串等），并执行其中的代码块。
如果在执行代码块的过程中满足某个条件，程序将执行break语句并跳出循环。
否则，当循环结束时，程序将执行else语句中的代码块。

"""

# 实例

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        print("I found the banana!")
        break
else:
    print("I searched everywhere, but could not find the banana.")

"""
在这个示例中，程序将遍历水果列表并查找香蕉。当程序找到香蕉时，它将打印"I found the banana!"，并执行break语句跳出循环。
否则，当循环结束时，程序将执行else语句中的代码块，并打印"I searched everywhere, but could not find the banana."
"""

# while else 也是一样的用法

"""
总结:
1. 循环次数确定,可以用for循环
2. while固定次数和不固定次数都行

"""









