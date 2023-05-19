# 1. 利用正则匹配QQ号
import re

# 不能用0开头, 至少是5位的整数
# [1-9]\d{4,}


# 2. 身份证号

test2 = 'dsf130429191912015219k13042919591219521xkk'

# 前面17位是数字, 后面一位是数字或者字母x
matches2 = re.findall('\d{17}[\dx]', test2)
print(matches2)  # ['130429191912015219', '13042919591219521x']

# 取出最后一位
matches2_1 = re.findall('\d{17}([\dx])', test2)
print(matches2_1)  # ['9', 'x']

# 将得到的身份证进行分组
matches2_1 = re.findall('(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([\dx])', test2)
print(matches2_1)  # [('130429', '1919', '12', '01', '521', '9'), ('130429', '1959', '12', '19', '521', 'x')]


# 3. 手机号
# 1[3-9]\d[9]

# 区分区号和号码, 区号可以是3位也可以是4位

phone = '010-12345678'

matches3 = re.match('(\d{3}|\d{4})-(\d{8})', phone)

print(matches3.group())  # 010-12345678
print(matches3.group(1))  # 010
print(matches3.group(2))  # 12345678






