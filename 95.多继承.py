
# 多继承是指一个子类可以继承多个父类的属性和方法。
# 子类可以拥有多个父亲, 并且具有所有父亲的属性和方法
# 下面是一个Python的示例代码

# 定义父类1
class Parent1:
    def __init__(self):  # 父1的类属性是name = Parent1
        self.name = "Parent1"

    def greet(self):  # 父1 有一个greet方法
        print(f"Greetings from {self.name}!")  # Greetings from Parent1

    def method1(self):
        print(f"This is method1 from {self.name}.")  # This is method1 from Parent1


# 定义父类2
class Parent2:
    def __init__(self):
        self.name = "Parent2"

    def greet(self):
        print(f"Greetings from {self.name}!")

    def method2(self):
        print(f"This is method2 from {self.name}.")


# 定义父类3
class Parent3:
    def __init__(self):
        self.name = "Parent3"

    def greet(self):
        print(f"Greetings from {self.name}!")

    def method3(self):
        print(f"This is method3 from {self.name}.")


# 定义子类，继承自Parent1, Parent2和Parent3
class Child(Parent1, Parent2, Parent3):
    def __init__(self):          # 初始化属性
        Parent1.__init__(self)   # 继承父1的类属性
        self.age = 10

    def greet(self):
        print(f"Greetings from {self.name}! I'm {self.age} years old.")


# 创建Child类实例
c = Child()

# 继承了父1的类属性
print(c.name)  # Parent1

# 子类自己有的方法
c.greet()   # Output: Greetings from Parent1! I'm 10 years old. 注意这里的name在p1中被定义

# 调用从父类继承来的方法和属性
c.method1() # Output: This is method1 from Parent1.
c.method2() # Output: This is method2 from Parent2.
c.method3() # Output: This is method3 from Parent3.










