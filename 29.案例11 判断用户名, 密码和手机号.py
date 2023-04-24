"""
需求
用户名: admin123  手机号: 15811119999  密码:200325

1. 用户名或手机号+密码登录
2. 用户名, 由字母和数字组成, 字母全部小写, 首字母不能是数字,长度必须6位以上
3. 手机号, 纯数字, 长度11
4. 密码必须是6位数字
5. 以上符合条件,进行下层验证:判断用户名+密码 是否正确  正确成功否则失败


"""
flag = True

while flag:  # 确保如果格式不正确, 可以一直输入用户名和手机号
    name = input("请输入用户名或手机号:")
    if name.isdigit() and len(name) == 11 or name.islower() and name[0].isalpha() and len(name) >= 6:  # 用户名输入成功, 允许输入密码
        while True:  # 确保如果格式不正确, 可以一直输入密码
            password = input('请输入密码:')
            if password.isdigit() and len(password) == 6:  # 密码格式正确, 开始验证是否是正确的用户名和密码
                if (name == 'admin123' or name == '15811119999') and password == '200325':
                    print('用户登录成功!')
                    flag = False
                    break  # 登录成功也不再输入密码
                else:
                    print('用户名和密码有误, 请重新输入')
                    break  # 报错就跳出输入密码的循环, 重新输入用户名
            else:
                print('密码格式不正确, 请重新输入')
    else:
        print('用户名或手机号格式不正确, 请重新输入')































