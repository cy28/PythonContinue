"""
break 是用来结束整个循环,一般用于死循环中，结束死循环
continue 是用来跳出当前循环，然后开始下一轮循环
"""

"""
举例1：break的使用：输出1-5 然后num==3后面的数字不输出 (输出的结果是1,2）

num = 1
while num < 6:
    if num == 3:
        break
    else:
        print(num)
    num += 1

"""

"""
举例二：continue的使用 当num == 3时，不输出这个值，继续后面的输出

"""
num = 0
while num < 5:
    if num == 3:
        num += 1
        continue  # 这里跳出了当前的循环，重新判断 num<5 ,开始一轮新的循环
    print(num)
    num += 1








