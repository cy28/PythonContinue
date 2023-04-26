"""
需求:
    1. 定义book 包括书名 价格 作者
    2. 定义一个books[]列表可以放多本书
    3. 循环添加三本书 不能添加同名书籍
"""

books = []

while True:
    if len(books) == 3:
        break
    else:
        name = input('输入书名: ')
        for i in books:
            if name == i.get('书籍名称'):
                print('书名重复')
                break
        else:  # 找完了, 发现没有重复的书名, 于是执行下面的代码
            author = input('输入作者: ')
            price = input('输入价格: ')
            books.append({'书籍名称': name, '作者': author, '价格': price})























