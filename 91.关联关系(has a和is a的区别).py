"""
公路(Road)
属性: 公路名称 公路长度

车(Car)
属性: 车名 时速
方法1: 车在那条公路上以多少时速行驶了多长时间
方法2: 初始化车的属性, __init__方法
方法3: 打印对象, 显示车的属性信息

"""
import random


class Road:
    def __init__(self, name, len):
        self.name = name
        self.len = len


class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def get_time(self, road):
        time1 = random.randint(1, 10)
        msg = f'{self.brand}品牌的车在{road.name}上以{self.speed}km的速度行驶{time1}小时'
        print(msg)

    # 自定义对象的字符串表示
    def __str__(self):
        return f'品牌: {self.brand}, 速度: {self.speed}'


# 创建路的实例对象
road1 = Road('京藏高速', 12000)

# 创建车的实例对象
car1 = Car('奥迪', 120)

# 显示属性信息
print(car1)  # 品牌: 奥迪, 速度: 120


car1.get_time(road1)

# -----------------------------------------------------------------------------------------------------------------------

"""
"has a"和"is a"是面向对象编程中常用的两个概念。

"has a"表示一个对象包含另一个对象，通常使用组合实现。例如，一个车对象可以包含多个轮子对象，一个人对象可以包含多个器官对象。这种关系体现了一个对象与另一个对象之间的“拥有关系”。

"is a"表示一个对象是另一个对象的一种类型，通常使用继承实现。例如，一个狗对象是一个动物对象的子类，一个长方形对象是一个图形对象的子类。这种关系体现了一个对象与另一个对象之间的“种类关系”。

总之，“has a”强调的是对象之间的组合关系，即一个对象包含另一个对象；而“is a”强调的是对象之间的继承关系，即一个对象是另一个对象的一种类型。

"""


# "has-a"示例  # 一个类中使用了另一个类
class Car:
    def __init__(self, engine):
        self.engine = engine


class Engine:
    def start(self):
        print("Engine started")


my_engine = Engine()
my_car = Car(my_engine)  # 传入的是一个类实例

my_car.engine.start()  # 车传入一个引擎实例对象, 就可以调用引擎的方法

# --------------------------------------------------------------------------------------------------------


# "is-a"示例
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):  # 传入的是一个大类 相当于狗这个类有动物这个大类的属性
    def bark(self):
        print("Woof!")


my_dog = Dog("Fido")
print(my_dog.name)
my_dog.bark()


# 在上面的代码示例中，我们定义了两个类：Car和Engine。Car类"has-a"一个引擎（即Engine对象），因为一个汽车需要一个引擎才能运转。
# 因此，Car类的构造函数__init__接受一个Engine对象作为参数，并将其存储在self.engine属性中。
# 然后我们通过my_car.engine.start()来调用Engine对象的start()方法，启动汽车引擎。

# 另一个例子是Animal和Dog类。Dog类是一个Animal类的子类，因此它"is-a"一种动物。
# 但是，Dog类还有一个额外的方法bark()，用于表示狗的叫声。我们创建了一个Dog对象my_dog，并访问了它的name属性和bark()方法。
# 由于Dog类是Animal类的子类，因此my_dog对象也拥有Animal类中定义的__init__方法和name属性。














