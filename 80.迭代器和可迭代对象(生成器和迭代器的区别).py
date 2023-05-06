# 可迭代的对象: 1. 生成器 2. 元组 列表 集合 字典 字符串

# 如何判定一个对象是否是可迭代?
from collections.abc import Iterable
list1 = [1, 2, 3, 4, 5]
print(isinstance(list1, Iterable))  # 判断实例 True

print(isinstance('abcdef', Iterable))  # True

g = (x + 1 for x in range(6))
print(isinstance(g, Iterable))  # True

# 迭代器 可以被next()函数调用并不断返回下一个值的对象称为迭代器: Iterator
"""
迭代器（Iterator）是一个访问集合元素的方式，它提供了一种顺序访问集合中每个元素的方法，而不需要事先知道集合的大小。

在 Python 中，迭代器是一个实现了 __iter__() 和 __next__() 方法的对象。__iter__() 方法返回迭代器对象本身，__next__() 方法返回集合中的下一个元素。

当没有更多元素时，__next__() 方法会抛出 StopIteration 异常。

"""

# 问题1 可迭代的 是不是肯定就是迭代器?

"""
答案是不一定
生成器是可迭代的, 也是迭代器
列表list是可迭代的, 但不是迭代器
"""

# 问题2 可不可以将一个列表变成一个迭代器

"""
可以, 利用系统自带的iter()函数, 可以将列表变成一个迭代器
"""
list2 = [1, 2, 3, 4]
list2 = iter(list2)

print(next(list2))  # 1
print(next(list2))  # 2

# 问题3 生成器和迭代器的区别
"""
1. 生成器是为了节省内存, 一个一个拿到元素
2. 迭代器, 只要能调用next得到下一个元素的
3. 生成器是迭代器的一种
    生成器（Generator）是一种特殊的迭代器，它是由函数使用 yield 关键字生成的。
    相比于普通迭代器，生成器更加灵活、简洁、高效，并且可以延迟生成数据，逐步返回结果。
4. 列表, 元组等也能变成迭代器, 借助iter()函数
"""































