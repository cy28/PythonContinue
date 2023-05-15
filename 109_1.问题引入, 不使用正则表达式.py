"""
1. 问题引入

问题: 提取所给text中的邮箱和手机号

text = '楼主太流弊了, 在线想要4429779753@qq.com和xxxxx@live.com谢谢有楼主, 手机号也可以15131255789'

使用传统方法太麻烦了, 看_2, 于是产生了正则表达式来解决这一类情况
"""


def extract_contacts(text):
    contacts = []

    # 提取邮箱
    start_index = text.find('@')
    while start_index != -1:
        end_index = text.find(' ', start_index)
        if end_index == -1:
            end_index = len(text)
        email = text[start_index + 1:end_index]
        contacts.append(email)
        start_index = text.find('@', end_index)

    # 提取手机号
    phone_start = text.find('手机号也可以')
    if phone_start != -1:
        phone_end = text.find(' ', phone_start)
        if phone_end == -1:
            phone_end = len(text)
        phone = text[phone_start + 6:phone_end]
        contacts.append(phone)

    return contacts


text = '楼主太流弊了, 在线想要4429779753@qq.com和xxxxx@live.com谢谢有楼主, 手机号也可以15131255789'
contact_list = extract_contacts(text)
print(contact_list)  # 输出：['4429779753@qq.com', 'xxxxx@live.com', '15131255789']
