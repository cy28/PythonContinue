"""
设计模式：

设计模式是针对软件设计中的常见问题和场景，提出的一种解决问题的方法论，它是一套被广泛接受的通用的解决方案。
在Python中，设计模式是一种用于解决特定问题的可重用的方案，可以帮助开发人员更好地组织和管理代码，使其更易于维护、扩展和重用。
Python中常见的设计模式包括但不限于：单例模式、工厂模式、观察者模式、装饰器模式、适配器模式、策略模式等。
这些模式都是在特定场景下应用的最佳实践，它们可以帮助我们更好地组织代码并提高代码的可读性和可维护性。
"""


"""
单例设计模式是一种创建型设计模式，它确保一个类只能制造一个(对象)实例，并提供了一个全局访问点来访问该实例。
在单例模式中，一个类只能被实例化一次，无论在程序中的哪个地方都只能访问到同一个实例。
这个实例通常被保存在一个私有静态变量中，并提供一个公共的静态方法来访问该实例。
"""


class Singleton:
    _instance = None  # 用来存放对象的地址
    name = 'nei_nei'

    def __new__(cls):                               # 重写了object中的new方法
        if cls._instance is None:
            cls._instance = super().__new__(cls)    # 相当于object.__new__ 创建了一个对象, 用这个属性名接收该对象(地址)
            return cls._instance                    # 返回刚刚创建的对象
        else:
            return cls._instance

    def show(self, n):
        print(self.name, n)


s1 = Singleton()
s2 = Singleton()


print(s1)  # <__main__.Singleton object at 0x000001FFFD5BC220>
print(s2)  # <__main__.Singleton object at 0x000001FFFD5BC220>

print(s1.name)  # nei_nei
print(s2.name)  # nei_nei

s1.show(1)  # nei_nei 1
s2.show(2)  # nei_nei 2























