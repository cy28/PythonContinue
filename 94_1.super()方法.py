"""
super()函数用于调用父类的方法，从而实现继承和重载。是一个特殊的类

super()函数有两个参数：

1. 第一个参数是一个类，通常是子类，表示从哪个类开始查找父类。如果在多重继承的情况下使用super()函数，这个参数指定了查找父类方法的起点。

2. 第二个参数是一个对象，通常是self，表示当前实例对象。这个参数通常用于传递当前实例对象，以便让super()函数知道要查找哪个父类方法。

注意：super()函数有一个特殊的用法，即不传递参数。这种用法中，super()函数会自动根据当前上下文找到父类方法，并返回一个代理对象，可以直接调用父类方法。

"""


class Parent:
    def some_method(self):
        print("Parent method called")


class Child(Parent):
    def some_method(self):
        super().some_method()  # 相当于 super() = Parent
        print('Child method called')


# 在这个例子中，Child类继承了Parent类
# 在Child类的some_method()方法中，通过super()函数调用了父类的some_method()方法，从而实现了对父类方法的重载。
# 当我们调用Child类的some_method()方法时，将会输出：Parent method called


child1 = Child()
child1.some_method()
# Parent method called
# Child method called

