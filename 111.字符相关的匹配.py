# 字符相关
import re

# 1. 匹配固定的字符串, 匹配文本中的小明

text1 = "小明是一个聪明活泼的男孩，他有着一双大大的明亮眼睛。小明在学校是个很受欢迎的同学，因为他不仅学习好，而且乐于助人。" \
       "每当有同学遇到问题，小明总是第一个伸出援助之手。小明还是个多才多艺的孩子，他擅长绘画、弹钢琴和踢足球。" \
       "每周末，他都会参加艺术班的绘画课程，用画笔勾勒出美丽的图画。而在音乐方面，小明经常在家里弹奏美妙的曲子，"

# 使用re.findall()函数找到所有匹配的"小明"
matches1 = re.findall("小明", text1)

print('所有的小明: ', matches1)  # 所有的小明:  ['小明', '小明', '小明', '小明', '小明']
print("小明出现的次数：", len(matches1))  # 5


# 2. 匹配一位字符
# []: 表示匹配括号类的一位

test2 = '你好, zbhgha, 阿拉基发货嘎嘎, abi久啊放假啊合格, cdghhjv开朗互换avjjsjb, gh阿嘎嘎噶'

matches2 = re.findall('[abc]', test2)
print(matches2)  # ['b', 'a', 'a', 'b', 'c', 'a', 'b']

# 以g开头, 后面fgh任意一个字符的拼接
matches2_1 = re.findall('g[fgh]', test2)
print(matches2_1)  # ['gh', 'gh', 'gh']


# 3. 匹配除什么之外的任意字符

test3 = 'aahfahggasjashqgahfaghagj'

# [^...]: 匹配除了方括号内的字符之外的任意字符。

matches3 = re.findall('[^agh]', test3)
print(matches3)  # ['f', 's', 'j', 's', 'q', 'f', 'j']


# 4. 匹配一个区间
# -: 表示一个区间

test4 = '阿法拉jsaa说课稿卡机阿卡丽几个agaj, 1410985感觉hi起互感器'

matches4 = re.findall('[a-z]', test4)
print(matches4)  # ['j', 's', 'a', 'a', 'a', 'g', 'a', 'j', 'h', 'i']


matches4_1 = re.findall('[0-9]', test4)
print(matches4_1)  # ['1', '4', '1', '0', '9', '8', '5']


# 5. 匹配任意字符
# .: 匹配除换行符外的任意字符。

test5 = 'aljafjaghahiqshkljg'

# 匹配一位
matches5 = re.findall('g.a', test5)
print(matches5)  # ['gha']

# +: 匹配前一个字符的一次或多次重复。
# 遵循贪婪匹配, 匹配最长的
matches5_1 = re.findall('g.+h', test5)
print(matches5_1)  # ['ghahiqsh']

# 非贪婪匹配 加一个?号  相当于只加了一次
# ?: 匹配前一个字符的零次或一次重复。
matches5_2 = re.findall('g.+?h', test5)
print(matches5_2)  # ['ghah']


# 6. 匹配字母、数字和下划线(也可以匹配中文)
# 在计算机科学和编程领域，\w通常是表示"word"（单词）的缩写。
# 正则表达式中的\w代表单词字符（word character），可以匹配字母、数字和下划线。它是一个常用的元字符，用于匹配文本中的单词部分。


text6 = "Hello, world! This is an example."

matches6 = re.findall("\w+", text6)
print(matches6)  # ['Hello', 'world', 'This', 'is', 'an', 'example']

# 7. 匹配数字
# 在正则表达式中，\d是表示"digit"（数字）的缩写。它用于匹配数字字符，可以理解为匹配0到9之间的任意一个数字。

text7 = "I have 10 apples and 5 oranges."

matches7 = re.findall("\d+", text7)
print(matches7)  # ['10', '5']


# 8. 匹配任意空白符
# 在正则表达式中，\s是表示"whitespace"（空白字符）的缩写。它用于匹配空格、制表符、换行符和其他一些不可见的空白字符。


text8 = "Hello\tworld\nThis is an example."

matches8 = re.findall("\s", text8)
print(matches8)  # ['\t', '\n', ' ', ' ', ' ']











