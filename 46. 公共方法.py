"""
内置方法:
    1. print()
    2. input()
    3. type()
    4. id()    查看地址
    5. len()
    6. bin()
    7. oct()
    8. hex()
    9. chr()   ASCII码转字符
    10. ord()  字符转ASCII码 用于返回一个单字符字符串的 Unicode 码位
    # ord 是 "ordinal" 的缩写，意思是“序数的”，它表示字符在 Unicode 编码表中的位置或序号
关键字:
    1. del
    2. in
    3. not in
    4. is
"""

list1 = [1, 2, 3, 5, 17, 90, 0]

print(max(list1))  # 求最大值  90

print(min(list1))  # 求最小值  0

print(sum(list1))  # 求和  118

print(abs(-2))  # 求绝对值  2


list2 = (12, 34, 56, 6, 23, 44)

# sorted 是一个系统方法 返回的是一个排序好的列表
print(sorted(list2))  # [6, 12, 23, 34, 44, 56]


# 符号 + - * & |
# + 支持 字符串 列表 元组
# * 支持 字符串 列表 元组

list3 = [1, 2]

list4 = list3 * 4
print(list4)  # [1, 2, 1, 2, 1, 2, 1, 2]  相当于四个字符串相加

# - & | 只能用于集合, 表示 交集 intersection(&)  并集 union(|)   差集 difference(-)










