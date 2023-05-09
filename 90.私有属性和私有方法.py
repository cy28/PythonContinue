# 在Python中，私有属性和方法可以通过在属性或方法名称前面添加两个下划线“__”来定义。
# 他们都只能在在类的内部, 被访问或者调用
# 可以隐藏属性, 不能被外部随意修改; 也可以修改, 通过实例函数

class Person:

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.__sex = sex  # 私有属性：在属性名称前加__

    # 访问私有属性
    def get_sex(self, password):
        if password == "TOM":
            return self.__sex

    # 修改私有属性
    def set_sex(self, sex):
        self.__sex = sex
        return self.__sex


people1 = Person('lili', 18, 'female')

print(people1.name)  # lili

print(people1.age)   # 18

# print(people1.sex)   # 'Person' object has no attribute 'sex'
                       # 在类的外部不能直接访问对象的私有属性，需要在内部设置接口

# 要访问私有属性，可以通过类内部定义公有方法来实现。
# 公有方法可以访问私有属性并返回其值，然后在类外部调用该公有方法以获取私有属性的值。

print(people1.get_sex('TOM'))  # female

# 在上述代码中，私有属性 "__age" 只能在类内部访问。
# 但是，公有方法 "get_age()" 可以在类外部被调用，并返回私有属性的值。
# 可以在内部设置一个访问条件，外部符合条件，才允许调用这个外部方法
# 通过调用公有方法 "get_age()"，我们可以获取 Person 实例的私有属性 "__age" 的值

print(people1.set_sex('male'))  # male

# -------------------------------------------------------------------------------------------------------------------
# 私有方法


class MyClass:
    def public_method(self):
        print("Calling public_method")
        self.__private_method()

    def __private_method(self):
        print("Calling private_method")


my_object = MyClass()
my_object.public_method()


"""
1. 定义了一个名为 MyClass 的类，其中包含一个公共方法 public_method 和一个私有方法 __private_method。
2. 类中的公共方法可以调用私有方法。
3. 在类的外部，我们创建了一个 MyClass 的实例 my_object，然后调用了它的公共方法 public_method。
4. 当调用公共方法时，会先输出一行文本 "Calling public_method"，然后调用私有方法 __private_method。
5. 在私有方法中，也输出了一行文本 "Calling private_method"。

注意：
的是，私有方法的名称前面有两个下划线 __，这意味着它是一个私有方法，只能在类的内部使用。
在类的外部，我们无法直接访问或调用私有方法。
但是，在类的内部，我们可以通过 self.__private_method() 的方式来调用私有方法。
"""





























