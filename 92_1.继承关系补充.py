class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return '叫的方法'


class Dog(Animal):
    pass


dog = Dog('mimi', 3)

print(dog.name)     # mimi
print(dog.age)      # 3
print(dog.speak())  # 叫的方法

# super() 适用于子类的属性不与父类完全一致时, 去构建自己的属性

"""
例如:

    def __init__(self, name, age, breed):  
        super().__init__(name, age)         
        self.breed = breed     

"""

