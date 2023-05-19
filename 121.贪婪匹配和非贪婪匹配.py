# 1. 在正则表达式中，贪婪匹配是一种匹配策略，它尽可能多地匹配输入字符串中的字符。
# 在Python的正则表达式中，默认情况下，量词（如*、+、?、{}等）都是贪婪的，即它们会尽可能多次地匹配前面的表达式。


import re

string = "abcdef"
pattern1 = r"ab.*"

match1 = re.search(pattern1, string)
print(match1.group())

# 输出结果为："abcdef"。这是因为在正则表达式中，.*表示匹配任意字符（除了换行符）零次或多次。
# 贪婪匹配会尽可能多地匹配字符，所以.*会匹配整个字符串"abcdef"。


# 2. 然而，有时候我们可能希望匹配尽可能少的字符。在这种情况下，可以使用非贪婪匹配，即在量词后面添加?符号。非贪婪匹配会尽可能少次地匹配前面的表达式。


string = "abcdef"
pattern2 = r"ab.*?"

match2 = re.search(pattern2, string)
print(match2.group())

# 输出结果为："ab"。与之前的示例相比，正则表达式ab.*?ef中的.*?使用了非贪婪匹配。
# 它会尽可能少次地匹配任意字符，所以匹配结果为整个字符串"ab"。















