"""
需求:
1. 产生5组(不允许重复)的字母和数字组成的四位验证码
2. 打印这五组验证码
"""
import random
code_list = set()

s = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'

while True:
    code = ''  # 定义一个空字符串来存放验证码
    for i in range(4):
        r = random.choice(s)
        code += r
        # 将code添加到set中
    code_list.add(code)
    if len(code_list) == 5:
        break

print(code_list)
























