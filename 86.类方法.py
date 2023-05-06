# 类方法
"""
特点:
    1. 定义需要依赖装饰器@classmethod
    2. 类方法的参数不是一个对象, 而是类
    3. 类方法中只能使用类属性
    4. 类方法不能使用对象方法, 因为类方法在实例方法之前已经存在

"""


class Person:
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count += 1

    def say_hello(self):  # 这个方法必须依赖于self才存在, 所以是实例方法
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

    @classmethod
    def get_count(cls):  # cls是class的简写, 这里的cls相当于传入了Person
        print(f"There are {cls.count} people.")

# 这里定义了一个名为Person的类，它有三个成员：name、age和count。count是一个类级别的变量，用于记录创建了多少个Person对象。
# 该类还定义了两个方法：say_hello和get_count。say_hello方法是一个实例方法，用于输出该人的姓名和年龄。
# get_count方法是一个类方法，用于输出当前创建了多少个Person对象。
# 要使用该类，可以创建多个Person对象并调用get_count方法，例如：


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)
Person.get_count()   # 输出：There are 2 people.

# 在这个例子中，get_count方法被装饰为一个类方法，使用了@classmethod装饰器。
# 它的第一个参数是cls，代表该方法所属的类，可以通过它来访问类级别的变量。
# 在get_count方法内部，我们使用cls.count来获取Person类的count变量的值。这个方法不需要实例对象，可以直接通过类来调用。

















