# 在Python中，可以使用字符串的 `split()` 方法将字符串分割成子字符串列表。该方法将会按照指定的分隔符将字符串分割，如果没有提供分隔符，那么默认是以空格作为分隔符。

# 这是一些示例：


# 创建一个字符串
str1 = "Hello, world!"

# 使用split()方法将字符串分割成子字符串列表
str2 = str1.split()
print(str2)  # 输出： ['Hello,', 'world!']

# 使用逗号作为分隔符
str3 = str1.split(',')
print(str3)  # 输出： ['Hello', ' world!']

# 创建一个包含多个单词的字符串
str4 = "apple banana cherry"

# 使用split()方法将字符串分割成子字符串列表
str5 = str4.split()
print(str5)  # 输出： ['apple', 'banana', 'cherry']


# 还有一个 `splitlines()` 方法，它用于分割字符串到一个子字符串列表，其中每个子字符串对应字符串中的一行（由换行符分隔）。例如：


# 创建一个包含多行的字符串
str6 = "Hello\nworld"

# 使用splitlines()方法将字符串分割成子字符串列表
str7 = str6.splitlines()
print(str7)  # 输出： ['Hello', 'world']


# 注意，`split()` 和 `splitlines()` 方法都不会修改原始字符串，而是返回一个新的列表。
