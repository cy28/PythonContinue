# 1. re.match() 匹配字符串是否以指定的正则内容开头，匹配成功返回对象，匹配失败返回None

"""
re.match函数的参数包括：

1. pattern：要匹配的正则表达式模式。
2. string：要匹配的字符串。
3. flags：可选参数，指定匹配时的选项，如是否忽略大小写、是否多行匹配等。默认值为0，表示不使用任何选项。

"""

# 例1，使用re.match函数匹配一个字符串中的电话号码：
import re

pattern = r'\d{3}-\d{3}-\d{4}'  # 匹配xxx-xxx-xxxx格式的电话号码
string = '123-456-7890'
match_obj = re.match(pattern, string)
if match_obj:
    print('匹配成功！电话号码为：', match_obj.group())
else:
    print('匹配失败！')

"""
这个正则表达式模式用于匹配电话号码，其中：

1. \d 表示匹配任意一个数字字符。
2. {3} 表示前面的表达式\d需要匹配三次，即需要匹配三个数字字符。
3. - 表示匹配一个连字符。
4. \d{3}-\d{3}-\d{4} 表示需要匹配三个数字字符、一个连字符、三个数字字符、一个连字符、四个数字字符的字符串。
5. + 表示可以出现一次或者多次

"""


# 举例2 match一定从头开始匹配 开头不匹配 就返回空

test = "范冰冰 刘亦菲 杨幂 赵丽颖 周迅 林心如 马思纯 李冰冰 张雨绮 杨紫"

matches1 = re.match('范冰冰', test)
print(matches1)  # <re.Match object; span=(0, 3), match='范冰冰'>

matches2 = re.match('杨紫', test)
print(matches2)  # <re.Match object; span=(0, 3), match='范冰冰'>

























