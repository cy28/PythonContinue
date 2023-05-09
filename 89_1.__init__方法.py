"""
1.__init__
初始化魔术方法
触发时机：实例化对象时之后触发, 每实例化一次就执行一次
参数：一个self接收对象, 其他参数根据实例化的传参决定
返回值：无
作用：初始化对象的成员
注意：使用该方式初始化的成员都是直接写入对象当中，类中无法具有

"""


class Human:
    def __init__(self, name, age):
        # print('init方法被执行') # 每实例化一次就执行一次
        # print(self)  # <__main__.Human object at 0x00000237A54FC220>  self的地址和h1的地址是一样的
        # 为对象添加属性
        self.name = name
        self.age = age
        # 注意 括号里的age是init的形参, 而self.age中的age是对象的属性, 只是恰好名字一样

    def eat(self):
        print('吃饭方法')

    def run(self):
        print('跑步方法')

    def sleep(self):
        print('睡觉方法')


# 实例化一个人的对象
h1 = Human('张三', 20)  # 这一步实际有两步操作, 1. 制作一个对象(相当于有一块对象所在的内存空间), 2. 为对象初始化操作 实际上init发生在第二步
# print(h1)  # <__main__.Human object at 0x00000237A54FC220>














