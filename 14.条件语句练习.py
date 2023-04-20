# 1. 输入账号和密码（名：admin，密码1234）判断是否正确，正确显示登录成功，否则显示登录失败

#
# username = input('请输入你的用户名：')
# if username == 'admin':
#     password = input('请输入你的密码：')
#     if password == '1234':
#         print('登录成功')
#     else:
#         print('密码输入错误')
# else:
#     print('账号输入错误')
#

# 2. 键盘输入一个四位整数，判断百位数和十位数的数字相加和是否大于10.如果大于10显示success，否则显示fail

# number = int(input('请输入一个四位整数:'))
# if ((number % 10) + (number // 100) % 10) > 10:
#     print('success')
# else:
#     print('fail')


# 3. 产生两个随机数字1-10，判断两数字之和是否大于8且差小于3，如果是输出success，否则fail

import random

number1 = random.randint(1, 11)
number2 = random.randint(1, 11)
print(number1, number2)

if (number1 + number2) > 8 and abs(number1 - number2) < 3:
    print('success')
else:
    print('fail')



















