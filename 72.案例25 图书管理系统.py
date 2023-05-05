"""
复习:
os模块下的常用函数:

os.getcwd()         获取当前目录
os.listdir()        列出当前目录所含的内容, 并用列表的形式返回
os.mkdir()          创建文件夹
os.rmdir()          删除空的文件夹
os.remove()         删除文件
os.chdir()          切换目录


os.path常用函数:

os.path.dirname(__file__)           获取当前文件所在的文件目录(绝对路径)
os.path.join                        ('原路径', '需要', '拼接的', '路径'), 返回一个拼接后的路径
os.path.split()                     分割(文件目录, 文件名)
os.path.splittext()                 分割(文件目录/文件名, 扩展名后缀)
os.path.getsize()                   获取文件大小 , 以字节形式返回

os.path.isabs()                     判断是否是绝对路径
os.path.isfile()                    判断是否是文件
os.path.isdir()                     判断是否是目录
"""

# 通过文件将数据进行持久化保存, 后续会使用数据库保存数据


# 1. 用户注册  写文件
def register():
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    re_password = input('确认输入的密码: ')
    if password == re_password:
        # 保存信息
        with open('72_1.users.txt', 'a') as w_stream:
            w_stream.write(f'{username} {password}\n')
        print('用户注册成功!')
    else:
        print('密码不一致, 请重新注册')


# register()

# 2. 用户登录  读文件 判断有没有这个人
def login():
    username = input('请输入用户名: ')
    password = input('请输入密码: ')
    if username and password:  # 当用户名和密码都不为空, 进行下一步
        with open('72_1.users.txt', 'r') as r_stream:
            while True:
                user = r_stream.readline()  # 每次读一行, 得到的形式是 aa 111\n
                if not user:  # 是空的时候执行下面的语句
                    print('用户名或密码输入错误')
                    break
                # input_user = '{} {}\n'.format(username, password)
                input_user = f"{username} {password}\n"
                if user == input_user:
                    print('用户登录成功!')
                    break


# login()

# 3. 展示图书


def show_books():
    print('-------------------图书馆中的书有:-------------------')
    with open('72_2.books.txt', 'r', encoding='utf-8') as r_stream:
        books = r_stream.readlines()  # 得到的是一个列表
        for book in books:
            print(book, end='')


show_books()



























