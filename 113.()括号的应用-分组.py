import re

# 1. ()用来确定提取的区域

# 在正则表达式中，\b 是一个特殊字符序列，表示单词边界（word boundary）。单词边界表示单词的开始或结束位置。

# 举例1
text = "Hello, my name is John Doe. I am from New York."
pattern = r"\b([A-Z][a-z]+)\b"

matches = re.findall(pattern, text)
print("Matches:", matches)  # Matches: ['Hello', 'John', 'Doe', 'New', 'York']


# 举例2

text1 = '楼主太流弊了, 在线想要4429779753@qq.com和xxxxx@live.com谢谢有楼主, 手机号也可以15131255789, 15131232458'

matches1 = re.findall('15131(2\d{5})', text1)
print(matches1)  # ['255789']


matches1_1 = re.findall('15(13)1(2\d{5})', text1)  # 列表里面套元组
print(matches1_1)  # [('13', '255789'), ('13', '232458')]


# 2. ()用来确定提取的区域+或条件

text2 = '楼主15131root太15131alex流弊了, 在线想要4429779753@qq.com和xxxxx@live.com谢谢有楼主, 手机号也可以15131255789, 15131232458'

matches2 = re.findall('15131(2\d{5}|r\w+太)', text2)

print(matches2)  # ['root太', '255789', '232458']


# 3. []和()的区别

# [ ] 用于定义一个字符集合，表示在该位置可以匹配方括号内的任意一个字符。
# () 用于创建一个捕获组，表示将其内部的表达式作为一个整体进行匹配，并在匹配成功时可以获取该组的内容。

# [abc] 表示可以匹配字符 'a'、'b' 或 'c' 中的任意一个。
# (163|qq|126) 匹配'163''qq''126'中的任意一个




