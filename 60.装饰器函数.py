"""
1. 为什么引入装饰器函数 ?

"""

# a. 一个公司的基础平台功能


# def f1():
#     print('f1')
#
#
# def f2():
#     print('f2')
#
#
# def f3():
#     print('f3')

# b. 其他部门调用这些功能

#
# f1()
# f2()
# f3()

# c. 现在想在这些功能的基础上加上一个验证功能, 需要遵循的开放封闭的原则, 已经实现的功能不能被修改, 但是可以被扩展
# 于是采用装饰器函数来解决这个问题

# def dec(func):
#     def inner():
#         # 验证1
#         # 验证2
#         # 验证3
#         func()
#     return inner


# @dec
# def f1():
#     print('f1')

# 2. 装饰器的定义


def decorator(func):   # 外层传入的是扩展的函数
    def wrapper():
        func()
        print('精装修')  # 内层函数对传入的函数进行扩展
    return wrapper      # 返回扩展好的函数


@decorator
def house():
    print('土胚房')
# 以上实际执行的是 decorator(house) 和 house = wrapper
# house已经变成了wrapper

house()
# 土胚房
# 精装修












