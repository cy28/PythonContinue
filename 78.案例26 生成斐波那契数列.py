# 通过函数来获取生成器
"""
步骤:
    1. 定义一个函数, 函数中使用yield关键字, 只要出现了yield, 函数不在是函数, 而变成生成器
    2. 调用该函数. 接收调用的结果. 该结果就是生成器
    3. 借助next(g)或者g.__next__()得到元素

"""

# 举一个简单的例子来说明问题

# def func():
#     n = 0
#     while True:
#         n += 1   # 暂停的位置在这一步
#         yield n  # 这里的yield相当于return加上暂停
#
#
# g = func()
# next(g)


def fib(length):
    a, b = 0, 1
    n = 0
    while n < length:
        yield b  # 返回b, 并暂停在这个位置, 再次调用, 会从这一句的下一句开始运行
        a, b = b, a+b
        n += 1
    return '已经给出所需长度的元素'  # 当达到length时, 继续调用, 返回一个提示

g = fib(4)

print(next(g))  # 1
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3
print(next(g))  # StopIteration: 已经给出所需长度的元素































