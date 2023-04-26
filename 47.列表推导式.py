"""
Python中的列表推导式（List Comprehension）是一种简洁的语法结构，用于生成新的列表。
它的基本形式为：[expression for item in iterable]，
其中expression是用于生成新列表中每个元素的表达式，item是迭代器中的每个元素，iterable是一个可迭代对象（如列表、元组、字符串等）。
在列表推导式中，可以使用条件表达式对迭代器中的元素进行过滤。例如：[expression for item in iterable if condition]，
其中condition是一个布尔表达式，用于筛选出满足条件的元素。
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]


list1 = ['62', 'hello', '100', 'world', 'high', 'human']
# list1 如果是以h开头的则将首字母大写, 不是以h开头的全部转大写
list2 = [i.title() if i.startswith('h') else i.upper() for i in list1]
print(list2)  # ['62', 'Hello', '100', 'WORLD', 'High', 'Human']


# 练习一
# 实现分组一个list里面的元素, 比如[1,2,3,4,5,6............100] 变成 [[1,2,3][4,5,6].........]

# 1. 先定义一个初始列表
a = [i for i in range(1, 10)]
print(a)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 2. 对列表进行分组 用for循环确定每一个分组的开头下标

b = [a[x: x+3] for x in range(0, len(a), 3)]
print(b)  # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# 练习二
# 找出给出列表中含有两个'e'的放在新列表中
# names = ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'joe', 'alice', 'wendy', 'sherry']
# name = [i.title() for i in names]
# print(name)
# 给定列表: ['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe', 'Alice', 'Wendy', 'Sherry']

list3 = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'], ['Alice', 'Jennifer', 'Wendy', 'Sherry']]

list4 = [j for k in list3 for j in k if j.count('e') == 2]
print(list4)





















