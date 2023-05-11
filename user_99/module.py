class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        if username == self.username and password == self.password:
            print('登录成功')
        else:
            print('登录失败')

    def show(self):
        print(self.username, self.password)

    def publish_article(self, article):  # 这里的article是对象类型
        print(self.username, '发表了文章', article.name)


if __name__ == '__main__':  # 与之前一样, 测试代码
    print('user')










