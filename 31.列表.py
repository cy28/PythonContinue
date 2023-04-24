"""
由于变量一次只能保存一个数据, 当我们想要保存多个数据时，我们就需要引入列表的概念

注意:
1. 列表中的元素可以是不同的数据类型
2. 使用[]来声明列表
3. 通过下标访问列表中的元素
"""

# 1. 定义一个空列表
list1 = []

# 2. 定义一个有内容的列表
list2 = ['1', '123', 'a', True]  # 列表中的元素可以是不同的数据类型

# 3. 通过下标获取列表中的元素
print(list2[1])  # 123

# 4. 切边操作也与字符串保持一致, 返回的仍是一个列表
print(list2[:2])  # ['1', '123']



























