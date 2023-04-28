def login(username, password):
    """
    用户登录函数
    :param username: 用户名
    :param password: 用户密码
    :return: 登录状态
    """
    if username == 'admin' and password == '123456':
        print('登录成功')
        return True
    else:
        print('登录失败')
        return False


login('1234', 1234)  # 鼠标放在函数名上, 会出现对函数的注释










