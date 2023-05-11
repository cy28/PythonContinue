# 当父类的方法不能满足子类的需求时, 可以对方法进行重写(override)
"""
重写父类方法有两种情况:
    1. 覆盖父类的方法
    2. 对父类方法进行扩展

"""

"""
1) 覆盖父类的方法
    
    如果在开发中, 父类的方法实现和子类的方法实现, 完全不同
    就可以使用覆盖的方式, 在子类中重新编写父类的方法实现
    具体的实现方式, 相当于在子类中定义了一个和父类同名的方法
    重写之后, 在运行时, 只会调用子类中重写的方法, 而不会调用父类封装的方法

"""


class Animal1:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound.")


class Dog1(Animal1):
    def make_sound(self):
        print("The dog barks.")


dog = Dog1("Fido")
dog.make_sound()  # Output: The dog barks.


"""
2) 对父类的方法进行扩展
    如果在开发中, 子类的方法实现中包含父类的方法实现
    父类原本封装的方法实现是子类方法的一部分, 就可以使用扩展的方式
    步骤:
        1. 在子类中重写父类的方法
        2. 在需要的位置使用super().父类的方法来调用父类方法的执行
        3. 代码其他的位置针对子类的需求, 编写子类特有的代码实现

"""


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is speaking...")

    def eat(self):
        print(f"{self.name} is eating...")

    def sleep(self):
        print(f"{self.name} is sleeping...")


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print("Woof! Woof!")

    def eat(self):
        super().eat()
        print(f"{self.name} is eating a bone...")

    def sleep(self):
        super().sleep()
        print(f"{self.name} is dreaming about chasing squirrels...")


animal = Animal("Generic Animal", 5)
dog = Dog("Fido", 3, "Golden Retriever")

animal.speak()  # 输出 "Generic Animal is speaking..."
animal.eat()  # 输出 "Generic Animal is eating..."
animal.sleep()  # 输出 "Generic Animal is sleeping..."

dog.speak()  # 输出 "Fido is speaking..."
dog.eat()  # 输出 "Fido is eating..." 和 "Fido is eating a bone..."
dog.sleep()  # 输出 "Fido is sleeping..." 和 "Fido is dreaming about chasing squirrels..."
dog.bark()  # 输出 "Woof! Woof!"






















