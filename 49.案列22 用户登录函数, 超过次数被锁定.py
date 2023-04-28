"""
需求:
    定义一个login函数
    admin 1234
    输入用户名和密码, 验证是否正确
    带参数, 表示允许输入的次数
"""


def login(n):
    count = 0
    while True:
        if count < n:
            username = input('输入用户名:')
            password = input('输入密码:')
            if username == 'admin' and password == '1234':
                print('用户登录成功')
                break
            else:
                print('用户登录失败, 请重新输入')
                count += 1
        else:
            print('登录失败次数超过限制, 用户被锁定')
            break

login(3)