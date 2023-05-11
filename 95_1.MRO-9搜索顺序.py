# MRO是Method Resolution Order的缩写，意为“方法解析顺序”。在Python中，MRO用于决定在多重继承的情况下，如何按照正确的顺序搜索方法和属性。

"""
在Python中，多继承的搜索顺序遵循所谓的"广度优先搜索"（BFS）算法。
BFS算法基于"先搜当前层级，再搜下一层级"的原则，保证在多继承的情况下，子类的方法和属性可以正确地覆盖父类的方法和属性。

搜索顺序遵循以下三个原则：

1. 从左到右，按照类定义时的顺序进行搜索。

2. 深度优先，即在每个类中先搜索当前方法，如果没有找到则继续向下递归搜索父类。

3. 避免重复搜索，即如果两个类都是某个类的直接或间接父类，则只搜索第一个父类。

具体地，搜索顺序遵循"C3算法"，它是一种广度优先搜索的算法，用于确定Python中多重继承的搜索顺序。
这个算法会根据类之间的继承关系创建一个"类继承图"，并计算出一个线性化的列表，该列表表示搜索类中方法和属性的顺序。这个列表被称为“方法解析顺序”（MRO）。


"""


import inspect


class Base:
    def test(self):
        print(Base)


class A(Base):
    def test(self):
        print('A' * 10)


class B(Base):
    def test(self):
        print('B' * 10)


class C(Base):
    def test(self):
        print('C' * 10)


# A, B, C 都是D的父类, 那么如果调用test, 会使用谁的test呢?
class D(A, B, C):
    pass


d = D()
d.test()  # AAAAAAAAAA

print(inspect.getmro(D))
# 搜索的顺序
# (<class '__main__.D'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.Base'>, <class 'object'>)


















