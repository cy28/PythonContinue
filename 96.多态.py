# 多态（polymorphism）是面向对象编程中的一个概念，指同一个方法或操作在不同的对象上具有不同的实现方式。
# 以下是一个示例，演示多态的概念：

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class Cow(Animal):
    def speak(self):
        return "Moo!"


def animal_speak(animal):
    print(animal.speak())


dog = Dog("Rufus")
cat = Cat("Whiskers")
cow = Cow("Bessie")

animal_speak(dog)  # 输出 "Woof!"
animal_speak(cat)  # 输出 "Meow!"
animal_speak(cow)  # 输出 "Moo!"


"""
在这个例子中，我们定义了一个 Animal 基类和三个子类：Dog、Cat 和 Cow。
每个子类都实现了 speak() 方法，但实现方式不同，分别返回不同的字符串。
我们还定义了一个函数 animal_speak()，接受一个 Animal 类型的参数，并调用参数的 speak() 方法。
在调用 animal_speak() 函数时，我们可以传入任何一个 Animal 子类的实例，因为每个子类都实现了 speak() 方法。
不同的子类会根据其实现方式返回不同的字符串，这就是多态的概念。

"""






























