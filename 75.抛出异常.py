# raise 抛出异常

def register():
    username = input('输入用户名: ')
    if len(username) < 6:
        raise Exception('用户名长度必须六位及以上')
    else:
        print('输入的用户名是: ', username)

register()

#     raise Exception('用户名长度必须六位及以上')
# Exception: 用户名长度必须六位及以上


























