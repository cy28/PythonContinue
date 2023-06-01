# 字符串的常见操作包括:
"""
1. 获取长度: len
2. 查找内容: find, index, rfind, rindex
3. 判断: startswith, endswith, isalpha, isdigit, isalnum, isspace, isupper, islower
4. 计算出现次数: count
5. 替换内容: replace
6. 切割字符串: split, rsplit, splitlines, partition, rpartition
7. 修改大小写: capitalize, title, upper, lower, swapcaese
8. 空格处理: ljust, rjust, center, lstrip, rstrip, strip
9. 字符串拼接: join +

注意: 在python中, 字符串是不可变的! 所有的字符串的相关方法, 都不会改变原来的字符串, 都是返回一个结果, 在这个新的返回值里, 保留了执行后的结果
"""

"""1. len() 获取字符串的长度"""

str1 = "我的电脑卡了，你的电脑卡吗？"

print(len(str1))  # 14


"""
2. 查找内容: find, index, rfind, rindex

       find() 从左往右查找, 只要符合一个符合要求的就返回位置, 如果没有找到任何符合要求的则返回-1, 如果找的是多个字符,则返回第一个字符的位置
       rfind (right find) 从右往左找, 但返回的还是从左往右顺序的正数
       index() 跟find一样, 区别在于找不到就报错
       rindex (right find) 从右往左找, 但返回的还是正数
"""
str2 = "https://www.google.com/search"

i = str2.find("w")
print(i)  # 153

j = str2.rfind("w")
print(j)  # 153


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


"""
 4. 计算字符出现次数: count 
"""
k = str2.count("M")
print(k)  # 1


""" 
5. 字符串替换 : replace(old, new, count)     在字符串中对指定内容进行替换
第一个参数:要替换的内容
第二个参数:替换后的内容
第三个参数；替换的次数
"""

str5 = "这个店铺的商品很垃圾，这么垃圾的商品还拿出来卖？"
print(str5)  # 这个店铺的商品很垃圾，这么垃圾的商品还拿出来卖？
print(str5.replace("垃圾", "**"))  # 这个店铺的商品很**，这么**的商品还拿出来卖？
print(str5.replace('垃圾', '**', 1))  # 这个店铺的商品很**，这么垃圾的商品还拿出来卖？


"""
6. 字符串分割  split, rsplit, splitlines, partition, rpartition
"""
# split("分隔符", maxsplit) 以指定字符对字符串进行分割(默认是空格) 分割后的结果放在列表中, maxsplit 表示最大的分割次数
str6 = "this is a string example"

print(str6.split())  # ['this', 'is', 'a', 'string', 'example'] 以空格为分割，切成列表的形式

print(str6.split("i"))  # ['th', 's ', 's a str', 'ng example']

# rsplit() 从右开始切割

# splitlines()  按行切割

str6_1 = """你来吃饭吧!
你来跳舞吧!
你来学习吧!
"""
print(str6_1.splitlines())  # ['你来吃饭吧!', '你来跳舞吧!', '你来学习吧!']

# partition() 将字符串分成三部分, 分隔符左边, 分隔符, 分隔符右边

print(str6.partition(" "))  # ('this', ' ', 'is a string example')


"""
7. 修改大小写: capitalize, title, upper, lower, swapcase()
"""
str7 = "I Miss you VERY much"

# upper() 括号里面不需要参数，将整个字符串变为大写
print(str7.upper())  # I MISS YOU VERY MUCH

# lower() 括号里面不需要参数，将整个字符串变为小写
print(str7.lower())  # i miss you very much

# swapcase()  # 将字符串大写变小写，小写变大写
print(str7.swapcase())  # i mISS YOU very MUCH

# title()  # 将英文单词中的每一个首字母，都变成大写
print(str7.title())  # I Miss You Very Much

# capitalize() # 将第一个首字母大写
print(str7.capitalize())  # I miss you very much


# 8. 空格处理: ljust, rjust, center, lstrip, rstrip, strip

"""
# 消除指定字符串
# strip（）去除字符串两边的指定字符（如果不指定，则默认是去除空格）
# lstrip() 只去除字符串左边的指定字符
# rstrip() 只去除字符串右边的指定字符
"""
str8 = "    today is a nice day    "
str8_1 = "****today is a nice day****"
print(str8)                   # today is a nice day
print(str8.strip())           # today is a nice day
print(str8_1)                 # ****today is a nice day****
print(str8_1.strip("*"))      # today is a nice day
print(str8_1.lstrip("*"))     # today is a nice day****
print(str8_1.rstrip("*"))     # ****today is a nice day


# center()   将给定字符放在正中央
str8_2 = 'center'
print(str8_2.center(30))  # 在30个字符中, 将center放在正中央

# ljust()  左对齐, 将字符放在最左边
print(str8_2.ljust(30))  # 在30个字符中, 将center放在最左边

# rjust()  右对齐, 将字符放在最右边


"""9. 字符串拼接: join +"""

# join()  以指定字符对字符进行拼接
str9 = "-"
tup = ("hello", "every", "body")
print(str9.join(tup))  # hello-every-body 将str4加入到tup
















