"""
1. 问题引入

问题: 提取所给text中的邮箱和手机号

text = '楼主太流弊了, 在线想要4429779753@qq.com和xxxxx@live.com谢谢有楼主, 手机号也可以15131255789

使用传统方法太麻烦了, 看_2, 于是产生了正则表达式来解决这一类情况
"""

import re


def extract_contacts(text):
    pattern_email = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'
    pattern_phone = r'\d{11}'

    emails = re.findall(pattern_email, text)
    phones = re.findall(pattern_phone, text)

    contacts = emails + phones
    return contacts


text = '楼主太流弊了, 在线想要4429779753@qq.com和xxxxx@live.com谢谢有楼主, 手机号也可以15131255789'

contact_list = extract_contacts(text)
print(contact_list)  # 输出：['4429779753@qq.com', 'xxxxx@live.com', '15131255789']
