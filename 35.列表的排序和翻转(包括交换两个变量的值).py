# 生成8个1-20之间的随机数, 保存到列表中, 并遍历打印
import random

numbers = []
for i in range(8):
    ran = random.randint(1, 20)
    numbers.append(ran)

print(numbers)  # [11, 11, 20, 12, 1, 14, 19, 11]

# reverse() 将列表元素进行翻转
numbers.reverse()
print(numbers)  # [11, 19, 14, 1, 12, 20, 11, 11]

# sort()  将列表中的数字从小到大排列, 默认是升序, 不会生成新列表
numbers.sort()
print(numbers)  # [1, 11, 11, 11, 12, 14, 19, 20]

# reverse=True  降序排列
numbers.sort(reverse=True)
print(numbers)  # [20, 19, 14, 12, 11, 11, 11, 1]

# sorted() 会把排序后的结果生成一个新列表，传入的参数是原列表
list1 = [12, 34, 21, 35, 6, 24]

list2 = sorted(list1)  # 默认是升序排列
print(list2)  # [6, 12, 21, 24, 34, 35]

# sorted() 还可以传入参数关键字，根据参数关键字进行排序
list3 = ['abc', 'mm', 'd', 'hello', 'word']
list4 = sorted(list3, key=len)
print(list4)  # ['d', 'mm', 'abc', 'word', 'hello']

# 交换两个变量的值
a = 2
b = 3
a, b = b, a

print(a, b)  # 3 2










