"""
3. 判断: startswith, endswith, isalpha, isdigit, isalnum, isspace  返回的都是bool类型
"""
str2 = "https://www.google.com/search"

# startswith 判断是否以什么开头
start1 = str2.startswith('http')
print(start1)  # True

# endswith 判断是否以什么结尾的, 一般用于判断文件名
end1 = str2.endswith("search")
print(end1)  # True

# isalpha 只有字符串才能调用, 判断字符串是否是纯字母,返回True和False
alpha_string = "Hello"
print(alpha_string.isalpha())  # True

# isdigit 只有字符串才能调用, 判断字符串是否是纯数字,返回True和False
digit_string = "123456"
print(digit_string.isdigit())  # True

# isalnum 只有字符串才能调用, 判断字符串是否是字母和数字,返回True和False
alnum_string = "Hello123"
print(alnum_string.isalnum())  # True

# isspace 只有字符串才能调用, 判断字符串是否只包含空格,返回True和False
space_string = '    '
print(space_string.isspace())  # True

# isupper()  判断字符串中的字母是否全部是大写
print('HELLO'.isupper())  # True

# islower()  判断字符串中的字母是否全部是小写
print('hello'.islower())  # True
