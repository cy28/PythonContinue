# 1. 函数内部局部变量
"""
# a. 查看局部变量
def outer():
    a = 100

    def inner():
        b = 200
        print('我是内部函数')
    results = locals()  # 查看函数内部的局部变量, 以字典的形式返回
    print(results)


outer()  # {'a': 100, 'inner': <function outer.<locals>.inner at 0x00000206E778DAB0>}
"""

# b. outer内部调用inner
"""
def outer():
    a = 100

    def inner():
        b = 200
        print('我是内部函数')
    inner()


outer()  # 我是内部函数
"""

# c. 想在inner内部修改变量a, 使用关键字nonlocal


def outer():
    a = 100

    def inner():
        b = 200
        nonlocal a  # 想改外层函数的变量, 得加关键字nonlocal
        a += b
    inner()
    print(a)

# 函数需要使用变量时, 总是先从内部寻找该变量, 如果没有, 再到外层函数中寻找该变量


outer()  # 300

# 2. 函数嵌套
# 函数嵌套是指在一个函数内部定义另一个函数的过程。
# 在Python中，函数嵌套允许开发者将一个函数的某些功能抽象出来，形成一个新的函数。
# 这种方式可以让代码更加模块化，减少重复代码的编写，提高代码的复用性。


def t1():
    t2()
    print(111)


def t2():
    t3()
    print(222)


def t3():
    print(333)


t1()
# 333
# 222
# 111

# 整个过程仍然符合先定义，再使用，是现将所有的函数先定义一遍，再调用函数

























