"""
2. 查找内容: find, index, rfind, rindex

       find() 从左往右查找, 只要符合一个符合要求的就返回位置, 如果没有找到任何符合要求的则返回-1, 如果找的是多个字符,则返回第一个字符的位置
       rfind (right find) 从右往左找, 但返回的还是从左往右顺序的正数
       index() 跟find一样, 区别在于找不到就报错
       rindex (right find) 从右往左找, 但返回的还是正数
"""

str2 = "https://www.google.com/search"

i = str2.find("w")
print(i)  # 8

j = str2.rfind("w")
print(j)  # 10

# 需要注意的是:
# 1. 索引从0开始
# 2. 返回的索引都是从左往右的索引值
