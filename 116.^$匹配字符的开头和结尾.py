#  ^: 匹配字符串的开头。
#  $: 匹配字符串的结尾。
# 为什么使用?
# 确保字符从开头一直匹配的结尾, 否则如果中间有符合条件的, 也会匹配成功
import re

# 举例1 用户名可以是字母或者数字, 不能是数字开头, 用户名长度必须六位以上

username1 = '123asdfgh'

username2 = 'admin12345'

username3 = '#$admin12345*&^'


# 不加开始结尾符
matches1 = re.search('[A-Za-z][A-Za-z0-9]{5,}', username1)
matches2 = re.search('[A-Za-z][A-Za-z0-9]{5,}', username2)
matches3 = re.search('[A-Za-z][A-Za-z0-9]{5,}', username3)

print(matches1)  # <re.Match object; span=(3, 9), match='asdfgh'>
print(matches2)  # <re.Match object; span=(0, 10), match='admin12345'>
print(matches3)  # <re.Match object; span=(2, 12), match='admin12345'>


# 加上开始结尾符
matches1 = re.search('^[A-Za-z][A-Za-z0-9]{5,}$', username1)
matches2 = re.search('^[A-Za-z][A-Za-z0-9]{5,}$', username2)
matches3 = re.search('^[A-Za-z][A-Za-z0-9]{5,}$', username3)

print(matches1)  # None
print(matches2)  # <re.Match object; span=(0, 10), match='admin12345'>
print(matches3)  # None

# 注意
# [A-Za-z0-9]可以改成[\w]




















