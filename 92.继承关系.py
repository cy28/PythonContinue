
"""
继承的概念: 子类拥有父类的所有方法和属性
继承是面向对象编程中的一种重要概念，它允许一个类（称为子类）从另一个类（称为父类或基类）继承属性和方法。
其目的是防止重复写代码

继承的语法:
class 类名(父类名):
    pass

子类继承自父类. 可以直接享受父类中封装好的方法, 不需要再次开发
子类中应该根据职责, 封装子类特有的属性和方法

"""

# 下面是一个简单的代码示例，演示如何使用Python实现继承：
# 情况一 如果父类有init且子类也有init的情况


# 父类
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return '叫的方法'


# 子类
class Dog(Animal):                          # 在子类中继承父类，只需要在参数列表中写上父类名即可
    def __init__(self, name, age, breed):   # 先初始化
        # 有两种继承父类构造函数的写法
        # 第一种，通过父类名字调用父类的构造函数
        # Animal.__init__(name, age)        # 再继承父类属性
        # 第二种，隐式继承父类的构造函数
        super().__init__(name, age)         # 再继承父类属性 super()找到父类, 然后执行父类的init
        self.breed = breed                  # 初始化自己的属性

    # def speak(self):
    #     return "Woof!"


# 子类
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    # def speak(self):
    #     return "Meow!"


"""
解释：

1. 定义了一个名为Animal的基类，它具有两个属性（名称和年龄）和一个空的speak()方法。

2. 定义了两个派生类Dog和Cat，它们分别继承了Animal类，并分别添加了它们自己的属性和实现了speak()方法。

3. 在Dog和Cat类的构造函数中，我们使用了super()函数调用基类的构造函数，以便在子类中初始化名称和年龄属性。这样就可以避免在子类中重复编写基类的代码。

4. 最后，我们实现了每个类自己的speak()方法，这样每个派生类就可以根据自己的需要定义自己的声音。
"""

d1 = Dog('mimi', 5, '哈士奇')

print(d1.speak())  # 叫的方法


