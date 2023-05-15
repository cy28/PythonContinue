import re

# 1. * 重复出现0次或者更多次(可以是一次)

test1 = '他是个大B个, 确实是个大2B'

matches1 = re.findall('大2*B', test1)
print(matches1)  # ['大B', '大2B']


# 2. + 重复1次或者更多次

test2 = '他是个大B个, 确实是个大2B, 大3B, 大6666666B'

matches2 = re.findall('大\d+B', test2)
print(matches2)  # ['大2B', '大3B', '大6666666B']


# 3. ? 重复0次或1次

test3 = '他是个大B个, 确实是个大2B, 大3B, 大6666666B'

matches3 = re.findall('大\d?B', test3)
print(matches3)  # ['大B', '大2B', '大3B']


# 4. {n} 重复指定次数0次

text4 = "123 4567 89"

matches4 = re.findall("\d{3}", text4)
print(matches4)  # ['123', '456']


# 5, {n,} 重复n次或者更多次

text5 = "123 4567 89 123456789"

matches5 = re.findall("\d{3,}", text5)
print(matches5)  # ['123', '4567', '123456789']


# 6. {n,m} 重复n-m次 中间不能有空格


text6 = "123 4567 89 123456789"

matches6 = re.findall("\d{2,4}", text6)

# 贪婪匹配, 会按满足最大的情况匹配
print(matches6)  # ['123', '4567', '89', '1234', '5678']




























