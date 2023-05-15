"""
在正则表达式中，\b 表示单词边界的位置。它不匹配任何具体的字符，而是匹配单词与非单词字符之间的位置。

具体来说，\b 会匹配满足以下条件的位置：

当前字符是单词字符（字母、数字或下划线）；
前一个字符是单词字符，而当前字符是非单词字符（或字符串的开头）；
当前字符是单词字符，而下一个字符是非单词字符（或字符串的结尾）。

"""

import re

text = "Hello, World! This isapaale a queshi_test."

# 查找以 "is" 开头的单词
matches = re.findall(r"\bis\w*\b", text)
print(matches)  # 输出: ['isapaale']

# 查找以 "test" 结尾的单词
matches = re.findall(r"\b\w*test\b", text)
print(matches)  # 输出: ['queshi_test']

# 查找包含单词 "is" 的单词
matches = re.findall(r"\b\w*is\w*\b", text)
print(matches)  # 输出: ['This', 'isapaale']






















