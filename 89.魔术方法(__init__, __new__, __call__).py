# 魔术方法就是一个类/对象中的方法，和其他方法的不同是，魔术方法不需要调用！魔术方法会在特定时刻自动触发。

"""
1.__init__
初始化魔术方法
触发时机：实例化对象之后触发
参数：一个self接收对象, 其他参数根据实例化的传参决定
返回值：无
作用：初始化对象的成员
注意：使用该方式初始化的成员(属性)都是直接写入对象当中，类中无法具有

"""

"""
2.__new__
构造方法
触发时机： 在实例化对象时触发
参数：一个cls接收当前类, 其他参数根据实例化的参数决定
返回值：必须返回一个对象实例
作用：管理和控制对象的生成过程
注意：实例化对象是Object类底层实现，其他类继承了Object的__new__才能够实现实例化对象。
先触发__new__才会触发__init__ 
"""


class Person:
    def __new__(cls, name):
        print('__new__ is called')
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print('__init__ is called')
        self.name = name


person = Person('Alice')

# __new__ is called
# __init__ is called

# __new__方法是一个类方法，它在对象创建之前调用。它的作用是创建一个对象，并返回该对象的实例。
# __new__方法的第一个参数是该类，之后的参数和__init__方法一样，是用于初始化对象的参数。
# __new__方法通常用于定制不可变类型的对象，如tuple、str、int等。

# __init__方法是一个实例方法，它在对象创建之后调用。它的作用是初始化对象的属性。
# __init__方法的第一个参数是该实例，之后的参数和__new__方法一样，是用于初始化对象的参数。
# __init__方法通常用于定制可变类型的对象，如list、dict、set等。

"""
3.__call__
调用对象的魔术方法
触发时机:将对象当作函数调用时触发 语法: 对象名(__call__中需要的参数)
参数:至少一个self接收对象，其余根据调用时参数决定
返回值：根据情况而定
作用：可以将复杂的步骤进行合并操作，减少调用的步骤，方便使用
注意：无
"""


class MyFunction:  # 此时想把类当成函数调用, 加__call__即可
    def __call__(self, *args, **kwargs):
        print("I'm being called with args:", args, "and kwargs:", kwargs)


# 创建一个MyFunction对象
my_function = MyFunction()

# 调用MyFunction对象
my_function(1, 2, 3, a=4, b=5)

# 输出
# I'm being called with args: (1, 2, 3) and kwargs: {'a': 4, 'b': 5}

























