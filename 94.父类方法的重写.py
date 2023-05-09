# 当父类的方法不能满足子类的需求时, 可以对方法进行重写(override)
"""
重写父类方法有两种情况:
    1. 覆盖父类的方法
    2. 对父类方法进行扩展

"""


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound.")


class Dog(Animal):
    def make_sound(self):
        print("The dog barks.")


dog = Dog("Fido")
dog.make_sound()  # Output: The dog barks.


























