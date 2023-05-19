"""
re.split() 是 Python 中 re 模块提供的一个函数，用于基于正则表达式模式对字符串进行分割操作。
# 得到的元素全部放在一个列表中

该函数的语法如下：

re.split(pattern, string, maxsplit=0, flags=0)

pattern：要匹配的正则表达式模式，用于确定分割的位置。
string：要进行分割操作的源字符串。
maxsplit：可选参数，指定最大分割次数。默认为 0，表示进行所有可能的分割。
flags：可选参数，用于控制正则表达式的匹配方式，如忽略大小写、多行匹配等。
re.split() 函数的工作流程如下：

首先，它会根据正则表达式模式将源字符串分割为多个子字符串。
分割的依据是匹配到的模式。
分割完成后，它将返回一个包含分割后子字符串的列表。

"""

import re

text = "Hello, world! How are you?"
parts = re.split(r"[,.!? ]+", text)
print(parts)  # Output: ['Hello', 'world', 'How', 'are', 'you']






