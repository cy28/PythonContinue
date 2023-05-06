class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self, words):
        print(f"Hello, my words is {words}, my name is {self.name}, and I'm {self.age} years old.")

# 这里定义了一个名为Person的类，它有两个属性：name和age，以及一个名为say_hello的对象方法。
# say_hello方法用于输出该人的姓名和年龄。
# 要使用该类，可以创建一个Person对象并调用其say_hello方法，例如：


person1 = Person("Alice", 25)
person1.say_hello("你好")   # 注意: 实例方法也可以进行传参
# 输出：Hello, my words is 你好, my name is Alice, and I'm 25 years old.
































