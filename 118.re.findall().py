"""
re.findall 是 Python 中 re 模块提供的一个函数，用于在字符串中查找所有匹配某个正则表达式模式的非重叠子串，并返回一个包含所有匹配结果的列表。

函数签名如下：

re.findall(pattern, string, flags=0)
参数说明：

pattern：需要匹配的正则表达式模式。
string：要在其中进行匹配的字符串。
flags（可选）：用于修改正则表达式的匹配行为的标志。可以使用多个标志，通过按位或（|）操作符进行组合。
re.findall 函数会从字符串的起始位置开始，依次搜索并返回所有匹配模式的子串。返回的结果是一个列表，列表中的每个元素都是一个匹配的子串。

"""

import re

text = "Hello, my name is John. I live in New York."
matches = re.findall(r"\b\w+\b", text)
print(matches)
# ['Hello', 'my', 'name', 'is', 'John', 'I', 'live', 'in', 'New', 'York']



