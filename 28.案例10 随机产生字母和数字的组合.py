import random
# 1. 先定义一个空字符串
filename = ''

# 2. 建立一个所有的字母和数字集合的字符串
s = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890'

# 3. 得到字符串的长度
length = len(s)

# 4. 循环获取字符串的一个下标,通过一个下标索引到字母或者数字
for i in range(6):    # 循环六次
    index = random.randint(0, length-1)
    filename += s[index]   # 每次循环增加一个字符

# 5. 打印获得的字母和数字的组合
print(filename)
















