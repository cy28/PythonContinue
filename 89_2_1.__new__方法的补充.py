# 1. 当我们定义变量时, 如果没有传入父类, 就默认继承了object这个类

class Student:  # 相当于 class Student(object):
    pass

# 2. object中定义了__new__的方法, 我们在定义类的时候, 对该方法进行重写
# 原型是 object.__new__(self, *args, **kwargs)

# 3. 构建一个对象的过程


"""
person = Person('Jack')

# 先调用object中的__new__方法, 把类名传进去, 对象的参数传进去, 会返回一个对象, 用对象名接收
1. person = object.__new__(Person, 'Jack')

# 然后调用对象自己的__init方法, 传入对象的参数, 进行初始化
2. person.__init__('Jack')

"""






























