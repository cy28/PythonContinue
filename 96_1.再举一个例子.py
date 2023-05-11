class Person:
    def __init__(self, name):
        self.name = name

    def feed_pet(self, pet):
        # isinstance(obj, 类)  判断obj是不是类的对象或者是不是该类的子类
        if isinstance(pet, Pet):
            print(f'{self.name}喜欢养宠物{pet.role}, 昵称是{pet.nickname}')
        else:
            print('不是宠物类型, 不能养')


class Pet:
    role = 'pet'

    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def show(self):
        print(f'昵称: {self.nickname}, 年龄: {self.age}')


class Cat(Pet):
    role = '猫'

    def catch_mouse(self):
        print('抓老鼠')


class Dog(Pet):
    role = '狗'

    def mind_house(self):
        print('看家')


class Tiger:
    def eat(self):
        print('太可怕了, 能吃人')


# 创建宠物对象
cat1 = Cat('neinei', 2)

dog1 = Dog('huahua', 3)

tiger1 = Tiger()

# 创建养宠物的人1
person1 = Person('嘉伟')

person1.feed_pet(cat1)  # 嘉伟喜欢养宠物猫, 昵称是neinei

# 创建养宠物的人2
person2 = Person('鹏鹏')

person2.feed_pet(tiger1)  # 不是宠物类型, 不能养


# 在这里的feed方法中, 不管是不是pet类型都能传进去, 需要自己进行判断, 通过isinstance判断





