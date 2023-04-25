# 元组和列表类似，本质都是有序的集合
# 元组和列表的区别在于：
# 1. 元组用() 列表用[]
# 2. 列表中的数据可以修改，元组中的数据不能修改

# 1. 创建元组
tup1 = (12, 34, 6, 7, True, 'hello')  # 跟列表一样，里面可以放各种各样的数据类型
print(type(tup1))  # <class 'tuple'>
print(tup1)  # (12, 34, 6, 7, True, 'hello')

# 注意 若元组中的元素只有一个，需要在那一个元素后添加一个逗号, 才能将其声明为元组类型
tup2 = (12)  # 12
print(type(tup2)) # <class 'int'>

tup2_1 = ('aaaaa')
print(type(tup2_1))  # <class 'str'>

tup3 = (12,)
print(type(tup3))  # <class 'tuple'>

# 2. 访问元组中的元素 通过最后一个元素
print(tup1[1])  # 34
print(tup1[-1])  # hello  -1 就是元组的最后一个元素

# 3. 元组中的元素是不能修改的
# tup1[1] = 23
# print(tup1)  # 'tuple' object does not support item assignment

# 4. 合并元组，通过'+'实现
tup4 = (223, 79, 328)
tup5 = ('world', 'hello', True)
print(tup4 + tup5)  # (223, 79, 328, 'world', 'hello', True)

# 5. 判断元素是否在元组中，使用成员运算符，in or not in
print(223 in tup4)  # True
print(223 in tup5)  # False

# 6. 元组的切片 [开始下标：结束下标]
print(tup1[0:2])  # (12, 34)
print(tup1[-1:])  # ('hello',) 从最后一个开始截，到最后一个结束，于是只截取了一个
print(tup1[:3])   # (12, 34, 6)  截取的下标 0,1,2

# 7. len() 获取元组的长度
print(len(tup1))  # 6

# 8. 获取元组中的最大max，最小值min，针对元组中都是数字的情况
tup6 = (12, 345, 5678, 987, 67854)
print(max(tup6))  # 67854
print(min(tup6))  # 12

# 9. 其他数据数据类型转化为元组 tuple() # 会返回一个新元组，要用一个变量去接
list1 = [12, 34, 7865, True, 'hello']
print(type(list1))  # <class 'list'>

list2 = tuple(list1)
print(type(list2))  # <class 'tuple'>

# 10. 遍历元组

# 法一  用for in 进行遍历
for i in tup6:
    print(i)
# 12
# 345
# 5678
# 987
# 67854

# 法二 用enumerate() e+nume+rate 枚举的方式 将下标和对应的值遍历出来
for k, v in enumerate(tup6):
    print(k, v)
# 0 12
# 1 345
# 2 5678
# 3 987
# 4 67854

# 11. count()计数
list11 = ('a', 'b', 'c', 'a', 1, 'a', 2, 'a')
n = list11.count('a')
print(n)  # 4

# 12. index(查找元素, 开始位置, 结束位置) 索引 通过元素获取下标位置
index1 = list11.index('a')
print(index1)  # 0

index2 = list11.index('a', 4, 6 )
print(index2)  # 5








