# 方法的种类 : 普通方法 类方法 静态方法 魔术方法

"""
实例方法和普通方法的区别:
    实例方法是在类中定义的方法，可以通过类的实例来调用。普通方法是在类外部定义的函数，与类的实例没有直接关联。
"""


class Phone:
    brand = 'xiaomi'
    price = '3999'

    def call(self):  # self接收的是调用时的对象
        print(self)
        print('正在打电话.........')
        print('note', self.note)
        # 可以使用self访问到对象中的属性 但这里并不能保证每一个对象都有note属性 如果有对象没有, 则会报错

p1 = Phone()
print(p1)
# <__main__.Phone object at 0x00000175ED3CFEE0>

print('---------------------------------------------------------------------------------')

p1.note = '我是p1的note'
p1.call()
# <__main__.Phone object at 0x00000175ED3CFEE0> 这里可以看出self就是p1
# 正在打电话.........
# note 我是p1的note

print('-----------------------------------------------------------------------------------')

p2 = Phone()
p2.note = '我是p2的note'
p2.call()
# <__main__.Phone object at 0x000002A5834D3220>
# 正在打电话.........
# note 我是p2的note










