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

sum_target = 0
num1 = 0
target = int(input('请输入你要计算的累加和：'))

while num1 < target:
    num1 += 1
    sum_target += num1
print(sum_target)
























