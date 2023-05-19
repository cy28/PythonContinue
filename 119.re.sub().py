"""
re.sub() 是 Python 中 re 模块提供的一个函数，用于在字符串中执行正则表达式的替换操作。
sub是substitute（替代）的缩写。

该函数的语法如下：

re.sub(pattern, repl, string, count=0, flags=0)
pattern：要匹配的正则表达式模式。
repl：替换的字符串或者替换函数。
string：要进行替换操作的源字符串。
count：可选参数，指定最大替换次数，默认为 0 表示替换所有匹配项。
flags：可选参数，用于控制正则表达式的匹配方式，如忽略大小写、多行匹配等。
re.sub() 函数的工作流程如下：

首先，它会在源字符串中查找与正则表达式模式匹配的部分。
当找到匹配项时，它会使用 repl 参数指定的字符串或者函数来进行替换操作。
替换完成后，它会返回一个新的字符串，原始字符串不会改变。

"""

import re

text = "Hello, world!"
new_text = re.sub(r"world", "Python", text)
print(new_text)  # Output: Hello, Python!


# repl 参数还可以是一个函数，该函数接受一个匹配对象作为参数，并返回一个替换字符串。函数可以根据匹配对象的内容进行动态替换。
# 例如：


def uppercase(match):
    return match.group(0).upper()  # 在 match.group(0) 中，参数 0 表示匹配对象中的整个匹配项。


text = "hello, world!"
new_text = re.sub(r"\b\w+\b", uppercase, text)
print(new_text)  # Output: HELLO, WORLD!

# 上述例子中，使用 \b\w+\b 匹配单词，然后通过 uppercase() 函数将匹配到的单词转换为大写。
# 通过 re.sub() 函数，可以方便地在字符串中进行正则表达式的替换操作，实现灵活的文本处理功能。
