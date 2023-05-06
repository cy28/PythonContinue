# __名字__()被称为魔术方法

"""
构造函数
1. 构造函数是一种特殊类型的函数，用于在创建类的实例时初始化该实例的属性和状态。被称为类的构造器或者初始化方法。

2. 在Python中，构造函数的名称是__init__，它在创建类的实例时自动被调用。

3. 构造函数使用self参数来引用类的实例本身，并接受其他参数，这些参数用于初始化实例的属性。
"""

# 例如，在以下代码中，构造函数使用name和age参数来初始化Person类的实例属性：


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# 在创建Person类的实例时，构造函数会自动调用，并使用提供的参数来初始化实例的name和age属性。例如：


person1 = Person("John", 30)  # 实际上括号对应的调用, 调用的就是init函数, 里面的参数也是给init传参

# 在这个例子中，我们创建了一个名为"person1"的Person类的实例，构造函数使用"name"参数初始化person1对象的"name"属性，
# 并使用"age"参数初始化其"age"属性。
# 总之，构造函数是一种特殊的函数，用于初始化类的实例属性和状态，以确保实例在创建时具有正确的初始状态。
# 在Python中，构造函数的名称是__init__。

print(person1.name)  # John
print(person1.age)  # 30




















































