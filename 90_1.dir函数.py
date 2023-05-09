"""
dir是"directory"的缩写，表示目录或者文件夹的意思。
在Python中，dir()函数用于获取指定对象的属性和方法列表，相当于获取该对象的"目录"或者"文件夹"。
因此，dir()函数的名称也可以理解为"获取对象的目录"或"获取对象的文件夹"。
"""

# dir() 拿到一个attribute的列表


class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name}!")


p = Person("Alice", 25)

print(dir(p))  # ['_Person__age...........'name', 'say_hello'] 并没有出现私有属性age, 被隐藏


# 在上面的例子中，我们定义了一个Person类，该类包含name和age属性，并定义了一个say_hello方法来打印一条问候语。
# 当我们创建一个Person对象并使用dir()函数来获取它的所有属性和方法时，Python会返回一个字符串列表，其中包含了该对象的所有属性和方法名称。

# 私有化实际上进行了改名, 名字被改为_Person__age
# 于是可以在外部进行访问, 但是不建议这么做

print(p._Person__age)  # 25

































