"""
# 只找一次
re.search() 是 Python 中 re 模块提供的一个函数，用于在给定的字符串中搜索匹配某个正则表达式模式的第一个位置。

re.search(pattern, string, flags=0) 接受三个参数：
pattern：要匹配的正则表达式模式，可以是字符串形式或预编译的正则表达式对象。
string：要在其中进行搜索的字符串。
flags（可选）：用于指定匹配的特殊标志，例如是否区分大小写、多行模式等。

re.search() 函数的工作原理如下：
它从给定的字符串的开头开始逐个字符进行搜索，尝试找到与指定的正则表达式模式匹配的第一个位置。
一旦找到匹配的位置，就返回一个匹配对象（Match object），包含有关匹配的信息，例如匹配的文本、起始位置和结束位置等。
如果未找到匹配的位置，则返回 None。

"""


import re

# 定义输入字符串和要搜索的模式
input_str = "快速的棕色狐狸跳过了懒狗。"
pattern = "狐狸"

# 使用 re.search() 函数在输入字符串中查找第一个匹配项
match = re.search(pattern, input_str)

print(match)  # <re.Match object; span=(5, 7), match='狐狸'> 注意: 0开始


# 使用group()得到匹配的数据
print(match.group())  # 狐狸
