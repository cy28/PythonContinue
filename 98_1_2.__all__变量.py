# __all__只适用于带*号的情况

"""
在 Python 中，__all__ 是一个特殊的变量，用于指定在 from module import * 导入中哪些名称应该被导入到当前命名空间中。

具体来说，如果一个模块定义了 __all__ 变量，那么只有该变量中列出的名称会被导入到当前命名空间中。

如果没有定义 __all__ 变量，那么默认情况下，所有不以下划线开头的名称都会被导入。

下面是一个例子，演示了如何使用 __all__ 变量来指定在 from my_module import * 导入中哪些名称应该被导入到当前命名空间中：

"""

# my_module.py

# 定义两个变量，其中一个以下划线开头
my_variable = "Hello, world!"
_my_secret_variable = "Shh, it's a secret!"


# 定义一个函数
def square(x):
    return x * x


# 定义一个类
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says: Woof woof!")


# __all__ 变量指定哪些名称可以被导入
__all__ = ["my_variable", "square", "Dog"]

# 在上面的代码中，我们定义了 my_variable、_my_secret_variable、square() 和 Dog，并指定了 __all__ 变量来限制导入的名称。


# 现在，在另一个 Python 脚本中，我们可以这样导入模块

"""
# 导入 my_module 中的所有名称
from my_module import *

# 使用 my_variable 和 square()
print(my_variable)
print(square(5))

# 由于 __all__ 中没有包含 _my_secret_variable，因此这行代码会报错
print(_my_secret_variable)

# 使用 Dog 类
my_dog = Dog("Fido", 3)
my_dog.bark()  # 输出：Fido says: Woof woof!

"""

# 输出的结果如下:
# Hello, world!
# 25
# NameError: name '_my_secret_variable' is not defined
# Fido says: Woof woof!













