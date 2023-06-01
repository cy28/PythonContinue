"""
在 Python 中，我们可以使用字符串的 `replace()` 方法来替换字符串中的一部分。
`replace()` 方法需要两个参数：第一个参数是你要替换的部分，第二个参数是你要替换成的内容。你还可以提供一个可选的第三个参数，表示你要替换的次数
"""


# 这里有一些例子来说明这个方法的使用：


# 创建一个字符串
str1 = "Hello, world!"

# 使用replace()方法替换字符串中的一部分
str2 = str1.replace("world", "Python")
print(str2)  # 输出： "Hello, Python!"

# 创建一个字符串，其中包含多个相同的单词
str3 = "apple apple apple"

# 使用replace()方法替换字符串中的一部分，只替换一次
str4 = str3.replace("apple", "orange", 1)
print(str4)  # 输出："orange apple apple"

# 使用replace()方法替换字符串中的一部分，替换所有出现的单词
str5 = str3.replace("apple", "orange")
print(str5)  # 输出："orange orange orange"
