"""
图书管理系统
    1. 至少5本书
    2. library = [{'book_name': 'xxxx', 'author': 'xxxx', 'price': 100, 'number': 4}, {}, {}]
    3. 操作:
        1. 借书
        2. 还书
        3. 查询
        4. 查看所有
        5. 退出

"""
import time
library = [
    {'book_name': '西游记', 'author': '吴承恩', 'price': 100, 'number': 40},
    {'book_name': '水浒传', 'author': '施耐庵', 'price': 100, 'number': 40},
    {'book_name': '红楼梦', 'author': '曹雪芹', 'price': 100, 'number': 40},
    {'book_name': '三国演义', 'author': '罗贯中', 'price': 100, 'number': 40},
    {'book_name': '天珠变', 'author': '唐家三少', 'price': 100, 'number': 40}]

while True:
    choice = input('请选择要进行的操作: 1-借书 2-还书 3-查询 4-查看所有书籍 5-退出\n')
    if choice == '1':
        name1 = input('输入要借书的书名或者作者名: ')
        for i in library:
            if name1 == i.get('book_name') or name1 == i.get('author'):
                print('查询到书籍: %s, 当前该书籍的数量为: %d' % (i['book_name'], i['number']))
                numbers1 = int(input('输入借的数量: '))
                if numbers1 < i['number']:
                    print('当前书籍存在剩余, 可以借出')
                    i["number"] -= numbers1
                    time.sleep(2)
                    print('成功借出')
                    print()
                    break
                else:
                    print('当前书籍数量不够, 请重新选择')
                    break
            else:
                print('找不到指定的书籍, 请重新查找')
                break
    elif choice == '2':
        flag2 = True
        while flag2:
            name2 = input('输入归还书籍的名称: ')
            for j in library:
                if name2 == j['book_name']:
                    numbers2 = int(input('输入你要归还的本数: '))
                    j['number'] += numbers2
                    print('归还成功, 退出当前操作')
                    flag2 = False
                    break
                else:
                    print('图书管不存在该书目, 请重新输入')
    elif choice == '3':
        flag3 = True
        while flag3:
            name3 = input('请输入要查询书籍的名称或者作者的名称: ')
            for k in library:
                if name3 == k['book_name'] or name3 == k['author']:
                    print('查询到该书籍, 其信息如下: \n')
                    print('书籍名称' + '\t'*7 + '作者' + '\t'*7 + '价格' + '\t'*7 + '剩余数量')
                    print(k['book_name'], end='\t' * 7)
                    print(k['author'], end='\t' * 6)
                    print(k['price'], end='\t' * 7)
                    print(k['number'])
                    print()
                    flag3 = False
                    break
                else:
                    print('找不到指定书籍, 请重新查找')
                    break
    elif choice == '4':
        print('所有书籍信息如下: ')
        print('书籍名称' + '\t' * 7 + '作者' + '\t' * 7 + '价格' + '\t' * 7 + '剩余数量')
        for t in library:
            print(t['book_name'], end='\t' * 7)
            print(t['author'], end='\t' * 6)
            print(t['price'], end='\t' * 7)
            print(t['number'])
        print()
    elif choice == '5':
        print('操作结束, 退出')
        break
    else:
        print('无该操作项, 请重新选择')
