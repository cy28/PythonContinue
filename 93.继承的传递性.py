
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")


class Mammal(Animal):  # "Mammal" 是指哺乳动物的意思
    def walk(self):
        print(self.name, "is walking.")


class Dog(Mammal):
    def bark(self):
        print(self.name, "is barking.")


dog = Dog("Fido")
dog.walk()  # Output: Fido is walking.
dog.eat()   # Output: Fido is eating.
dog.bark()  # Output: Fido is barking.

"""
在这个例子中，我们定义了一个 Animal 类，它有一个名称属性和一个 eat() 方法。
然后我们定义了一个 Mammal 类，它从 Animal 类继承，并添加了一个 walk() 方法。
最后，我们定义了一个 Dog 类，它从 Mammal 类继承，并添加了一个 bark() 方法。
我们创建了一个名为 "Fido" 的 Dog 对象，并使用它的 walk()、eat() 和 bark() 方法。
由于 Dog 类从 Mammal 类继承，而 Mammal 类又从 Animal 类继承，因此 Dog 类同时继承了 Animal 类和 Mammal 类的属性和方法。这就是继承的传递性。

"""


































