"""
__str__
触发时机:使用print(对象)或者str(对象)的时候触发
参数：一个self接收对象
返回值：必须是字符串类型
作用：print（对象时）进行操作，得到字符串，通常用于快捷操作
注意：无
"""


# __str__是Python中的一种特殊方法（也称为“魔术方法”），用于定义对象的字符串表示形式。
# 当我们使用print()函数或者str()函数来打印对象时，Python会自动调用该对象的__str__方法来获取字符串表示形式并输出。
# 下面是一个简单的例子，演示了如何在类中定义__str__方法：


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"


p = Person("Alice", 25)

print(p)  # 输出：Person(name=Alice, age=25)


# 在上面的例子中，我们定义了一个Person类，该类包含name和age属性，并定义了一个__str__方法来返回一个格式化的字符串，表示该对象的属性。
# 当我们创建一个Person对象并使用print()函数来打印它时，Python会自动调用该对象的__str__方法，并将其返回值作为字符串输出到屏幕上。
# 需要注意的是，__str__方法的返回值必须是一个字符串对象，否则会导致类型错误。此外，__str__方法通常应该返回一个可读性好的字符串，以方便调试和阅读代码。


















