"""
匿名函数的语法如下：
lambda arguments: expression
注意:
    1. arguments 是匿名函数的参数列表，用逗号分隔。在上面的示例中，参数列表只有一个参数 x。
    2. expression 是匿名函数的返回值。在上面的示例中，返回值是 x * 2。
    3. 匿名函数通常用于只需要执行一次的简单函数，如果需要创建复杂的函数，还是应该使用常规函数定义来进行编写。
"""

# 举例1


def fn(num):
    return num ** 2


num1 = fn(3)
print(num1)  # 9


# 匿名函数实现求一个数字的平方

num2 = lambda num: num ** 2  # 匿名函数的返回值需要通过一个变量来接
print(num2(3))  # 9

# -----------------------------------------------------------------------------------------------

# 2.  匿名函数的使用场合, 一般是作为参数来使用时, 才写成匿名函数的形式


# 举例2

# 定义一个函数，该函数接受一个函数作为参数
def apply_operation(num, operation):
    return operation(num)


# 定义一个匿名函数并将其作为参数传递给另一个函数
result = apply_operation(5, lambda x: x * 2)

print(result)  # 输出结果为 10


