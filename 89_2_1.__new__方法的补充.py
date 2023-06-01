# 1. 当我们定义一个类时, 如果没有传入父类, 就默认继承了object这个类

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

# -----------------------------------------------------------------------------------------------------------------


"""
以下是在代码中补全 `__new__` 方法的示例：

```python
class Person:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 30)

# 输出实例对象的属性
print(person1.name)  # 输出: Alice
print(person1.age)   # 输出: 30
```

在上述代码中，我们在 `Person` 类中补全了 `__new__` 方法。在这个自定义的 `__new__` 方法中，我们使用 `super().__new__(cls)` 调用父类的 `__new__` 方法来创建实例对象。

请注意，这里我们没有对实例对象进行其他处理或返回不同的实例对象，因此这个自定义的 `__new__` 方法与默认的 `__new__` 方法相同。在这种情况下，我们可以省略显式定义 `__new__` 方法，因为默认的 `__new__` 方法已经能够满足需求。

最后，我们可以看到代码仍然能够正常创建 `Person` 类的实例对象，并成功访问到实例对象的属性。



"""



























