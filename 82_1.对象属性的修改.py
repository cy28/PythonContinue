class Person:
    def __init__(self, name):
        self.name = name


p1 = Person('Jack')

print(p1.name)  # print(p1.name)

p2 = p1

p3 = p2

p2.name = 'Tom'


print(p1.name)  # Tom
print(p2.name)  # Tom
print(p3.name)  # Tom

# 实际上p1, p2, p3都指向同一块实例的地址, 通过一个实例名的修改, 整个实例空间被修改







































