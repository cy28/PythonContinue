# 在Python中，@property是一种装饰器（decorator），用于将一个类的方法转换为属性，使其可以像属性一样访问。
# 这样做的好处是可以使代码更简洁、更易读，同时也可以控制属性的访问和修改权限。
# 通常，我们会在类中定义一个私有属性，然后通过getter和setter方法来访问和修改该属性。
# 但是，使用@property装饰器可以将getter方法转换为属性，从而可以像访问属性一样访问该私有属性。
# 下面是一个简单的例子，演示了如何使用@property装饰器将方法转换为属性：

# 视频举例
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @ property
    def age(self):
        return self.__age

    # def set_age(self, age):
    #     if 0 < age < 100:
    #         self.__age = age
    #     else:
    #         print('不在规定的范围内')
    #
    # def get_age(self):
    #     return self.__age
    #


s = Person('peng_peng', 20)

print(s.age)  # 加了装饰器, 就可以正常的调用


# gpt举例
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.__age = age   # 私有属性，前面加下划线

    @property  # 方法转化为属性
    def age(self):
        return self.__age   # getter方法，将方法转换为属性

    @age.setter  # 属性可修改的装饰器
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self.__age = value   # setter方法，用于修改私有属性


p = Person2("Alice", 25)

print(p.age)   # 访问私有属性，使用属性名age而非方法名age()
p.age = 30   # 修改私有属性，同样使用属性名age而非方法名age()
print(p.age)

# 下面这行代码会抛出ValueError异常
# p.age = -10































