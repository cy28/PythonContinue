"""
注意
1. 函数的返回值需要通过return关键字进行返回，函数在哪里调用，就把结果返回到了哪里
2. 若想使用返回后的结果，可以用变量接收，也可以直接输出
3. return后面的代码不会执行
4. 函数中若没有return关键字或者没有数据返回，则默认值是none
"""


def test():
    return "返回值"


# 用一个变量接收
cc = test()
print(cc)  # 返回值

# 直接输出
print(test())  # 返回值


# return关键字可以一次性返回多个数据，多个数据之间需要用，隔开，结果会以元组的形式返回

def fn1():
    return 12, 34, 'haha'


print(fn1())  # (12, 34, 'haha')




























