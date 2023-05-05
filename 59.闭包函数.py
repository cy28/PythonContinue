"""
闭包函数的特点:
    1. 是一个嵌套函数
    2. 内部函数引用了外部函数的变量
    3. 返回值是内部函数
"""

# 举例1


def outer1(x):
    def inner1(y):
        return x + y
    return inner1  # 返回的是函数的地址, 不能加括号

# 函数的地址 + () + 括号中传入的变量 = 函数调用


add = outer1(5)  # 这里传入的是inner函数需要的参数x, 然后将inner函数的地址给add
                 # 相当于这里add得到了inner函数的地址, 同时得到了inner函数所需参数x的一个参数

print(add(3))  # 8  传入inner函数所需的参数
# add这里直接进入的是inner函数


# 举例2


def outer2(n):
    a = 10

    def inner2():
        b = a + n
        print('内部函数', b)

    return inner2  # 注意是定义完内部函数之后, 在外部函数返回内部函数, 注意一下缩进
    # 返回的是函数的地址, 不能加括号


r = outer2(5)
r()


















