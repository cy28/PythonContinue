"""
如果一个函数在内部不调用其他函数, 而是自己本身的话, 这个函数就是递归函数

注意:
    1. 递归必须有出口, 即什么时候停止
    2. 每次递归都要向出口靠进
"""


# 举例1
# def a():
#     print('---------aaa--------------')
#     # 调用a函数
#     a()
#
# a()


# 举例2 打印1-10的数字

# def test(i):
#     if i == 10:    # 结束条件
#         print('10')
#     else:
#         print(i, end=' ')
#         i += 1
#         test(i)
#
#
# test(1)  # 1 2 3 4 5 6 7 8 9 10


# 举例3 打印1-10的累加和

def test1(n):  # n表示开头的数

    if n == 10:
        return 10
    else:
        return n + test1(n+1)  # 1 + 后面的和


print(test1(1))


def test2(n):  # n表示结尾的数

    if n == 1:
        return 1
    else:
        return n + test2(n-1)   # 10 + 前面的9项和


print(test2(10))


# 举例4 计算 1-10累乘的值

def test3(n):

    if n == 1:
        return 1
    else:
        return n * test3(n-1)


print(test3(10))  # 3628800














