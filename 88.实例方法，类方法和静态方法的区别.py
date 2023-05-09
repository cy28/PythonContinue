"""
区别：

1.  instance_method是一个实例方法，因为它的第一个参数是self，
    这个参数是在调用方法时自动传递的实例对象本身。
    必须传入self作为第一个参数, 可以访问实例变量, 只能通过实例名访问

2.  class_method是一个类方法，因为它使用@classmethod装饰器来定义。
    在方法内部，第一个参数是cls，它代表了类本身，而不是实例对象。
    可以访问类变量, 通过实例名或类名访问

3.  static_method是一个静态方法，因为它使用@staticmethod装饰器来定义。
    它没有任何默认参数，因此不能访问实例属性或类属性。
    不能访问类变量, 也不能访问实例变量; 通过实例名和类名访问
"""


class MyClass:
    type = 'human'  # 定义一个类属性

    #  构造方法
    def __init__(self, name, age):  # 初始化实例属性
        self.name = name            # 定义实例属性
        self.age = age              # self是一个特殊参数，用来表示将来要创建的对象

    # 实例方法  必须传入self作为第一个参数, 可以访问实例变量, 只能通过实例名访问
    def instance_method(self, food):            # 定义一个实例方法
        print("This is an instance method")
        print(self.name+'正在吃'+food)           # 实例方法可以访问实例属性

    # 类方法  可以访问类变量, 通过实例名或类名访问
    @classmethod                                # 定义一个类方法
    def class_method(cls):                      # 参数cls指的是类对象
        print("This is a class method")
        print(cls.type)

    # 静态方法 不能访问类变量, 也不能访问实例变量; 通过实例名和类名访问
    @staticmethod
    def static_method():
        print("This is a static method")


# 如何调用这些方法：

# 创建类实例(对象)
obj = MyClass('chen', 23)

# 1. 调用实例方法 需要访问到实例中的属性
obj.instance_method('红烧肉')     # This is an instance method
                                 # chen正在吃红烧肉

# 2. 调用类方法  需要访问到类中的属性

# a. 通过类名调用
MyClass.class_method()           # This is a class method
                                 # human

# b. 通过实例名调用 会自动传入实例所属的类
obj.class_method()               # This is a class method
                                 # human

# 3. 调用静态方法  类变量和实例变量都不能访问 可以通过类名直接调用 对类和实例一无所知
MyClass.static_method()          # This is a static method


