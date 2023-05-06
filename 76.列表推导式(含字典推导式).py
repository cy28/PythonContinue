"""
列表推导式（List Comprehension）是一种快速创建列表的方式，在 Python 中非常常用。列表推导式可以用一个简单的表达式来创建一个新的列表，

语法结构为：
[expression(表达式) for item(变量) in iterable(旧列表) if condition(条件)]

expression：表示要生成的新列表中每个元素所计算出的结果表达式。
item：表示原列表中的每个元素。
iterable：表示原列表，可以是一个可迭代对象，如列表、元组、集合、字符串等。
condition：表示条件表达式，用来筛选满足条件的元素，可省略。

"""

# 举例1 可以使用列表推导式来生成一个由 0 到 9 的平方组成的新列表
squares = [x*x for x in range(10)]
print(squares)  # 输出 [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# 举例2 过滤掉长度小于或等于三的人名, 然后将首字母大写
names = ['tom', 'tim', 'mary', 'jackson', 'queen', 'abc', 'steven', 'bob', 'haha']
new_names = [name.capitalize() for name in names if len(name) > 3]
print(new_names)  # ['Mary', 'Jackson', 'Queen', 'Steven', 'Haha']

# 底层实现, 如果不写成列表推导式, 就会比较的麻烦
# title() 将一句话中的每一个单词的首字母大写
# capitalize() 将一句话中的第一个首字母大写
new_list = []

for i in names:
    if len(i) > 3:
        i = i.capitalize()
        new_list.append(i)
print(new_list)  # ['Mary', 'Jackson', 'Queen', 'Steven', 'Haha']


# 举例3 将1-100之间能被3和5整除的数, 组成一个新列表

numbers = [number for number in range(1, 101) if number % 3 == 0 and number % 5 == 0]
print(numbers)
# [15, 30, 45, 60, 75, 90]


# 举例4 得到一个由元组构成的列表, 元组里面的元素包括一个偶数和一个奇数, 偶数的范围是0-4, 奇数的范围是0-9
# 先用一般方法, 封装成一个函数
def func():
    list1 = []
    for i in range(5):
        if i % 2 == 0:
            for j in range(10):
                if j % 2 != 0:
                    list1.append((i,j))
    return list1


list2 = func()
print(list2)
# [(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9)]
# 用列表推导式实现 注意后面的一个for相当于内层循环

list3 = [(x, y) for x in range(5) if x % 2 == 0 for y in range(10) if y % 2 != 0]
print(list3)
# [(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), (2, 1), (2, 3), (2, 5), (2, 7), (2, 9), (4, 1), (4, 3), (4, 5), (4, 7), (4, 9)]

# 练习1
# 给一个list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]] -------> [3, 6, 9, 5]
list4 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 3, 5]]
list5 = [i[-1] for i in list4]
print(list5)  # [3, 6, 9, 5]

# 列表推导式支持带有 if-else 的条件表达式，它的语法结构为：
# [expression_if_true if condition else expression_if_false for item in iterable]

# expression_if_true：表示满足条件时要生成的元素表达式。
# condition：表示条件表达式，用来判断是否满足条件。
# expression_if_false：表示不满足条件时要生成的元素表达式。
# item：表示原列表中的每个元素。
# iterable：表示原列表，可以是一个可迭代对象，如列表、元组、集合、字符串等。


# 举例5
dict1 = {'name': 'tom', 'salary': 5000}
dict2 = {'name': 'jack', 'salary': 8000}
dict3 = {'name': 'mary', 'salary': 4500}
dict4 = {'name': 'tim', 'salary': 3000}
list6 = [dict1, dict2, dict3, dict4]
print(list6)
# [{'name': 'tom', 'salary': 5000}, {'name': 'jack', 'salary': 8000}, {'name': 'mary', 'salary': 4500}, {'name': 'tim', 'salary': 3000}]
# 如果薪资大于5000, 则将工资加200, 如果薪资低于等于5000, 则将工资加500

list7 = [i['salary'] + 500 if i['salary'] <= 5000 else i['salary'] + 200 for i in list6]
print(list7)  # [5500, 8200, 5000, 3500]  # 取出得是薪水, 返回的也只能是薪水


# 举例6 可以使用列表推导式来生成一个由 0 到 9 的奇偶性标记组成的新列表：

numbers = [x if x % 2 == 0 else 'odd' for x in range(10)]
print(numbers)  # 输出 [0, 'odd', 2, 'odd', 4, 'odd', 6, 'odd', 8, 'odd']


# 字典推导式
dict1 = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'C'}
# 交换key值和value值的位置

dict2 = {v: k for k, v in dict1.items()}
print(dict2)  # {'A': 'a', 'B': 'b', 'C': 'd'}

# 注意: 如果存在重复的键, 后面的键会把前面的键覆盖掉


























