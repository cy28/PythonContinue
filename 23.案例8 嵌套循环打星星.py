"""
嵌套循环

1.  for循环 嵌套语法：
    for i in 序列:
        for j in 序列:
            循环体


2.    while循环 嵌套语法：
初始条件1:
    while 终止条件1:
        初始条件2：
        while 终止条件2：
            循环体
            更新条件2
        更新条件1
"""

# 1. 打一个矩形
n = 1
while n <= 5:
    print('*'*4)
    n += 1

# 2. 打一个三角形
n = 1
while n <= 5:
    print('*'*n)
    n += 1

# 3. 打一个倒三角

n = 5
while n >= 1:
    print('*'*n)
    n -= 1


