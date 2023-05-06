class Phone:
    brand = 'huawei'


print(Phone)  # <class '__main__.Phone'> 会创建一个类的内存空间， 相当于一个模子


p1 = Phone()  # 使用类创建对象
print(p1)  # <__main__.Phone object at 0x000001BA6B62CB80> 会创建一个对象的新的命名空间
print(p1.brand)  # huawei
p1.brand = 'iPhone'
print(p1.brand)  # iPhone

p2 = Phone()
print(p2.brand)  # huawei  p1的属性的修改并没有影响p2的属性， 说明每构建一个对象都会开辟一片新的内存空间

# --------------------------------------------------------------------------------------------------------------
# 定义类和属性


class Student:
    # 类属性
    name = 'xiaowei'
    age = 22


# 使用类, 创建对象
xiaowei = Student()

# 进行赋值操作时, 在其对象空间动态创建了自己的属性, 称为对象属性
xiaowei.age = 18

# 先在自己的对象空间中寻找值, 然后到类空间去找对应的值
print(xiaowei.age)  # 18

# 修改类属性, 模型的属性已将被修改成了fei_fei
Student.name = 'fei_fei'

xiao_hua = Student()
print(xiao_hua.name)  # fei_fei
















