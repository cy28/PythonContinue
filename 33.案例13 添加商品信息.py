"""
需求:
    1. 购买多件商品
    2. 记录每一件商品的名称,价格和数量

"""
container = []  # 存多件商品的容器

flag = True
while flag:
    name = input('请输入商品的名字: ')
    price = input('请输入商品的价格: ')
    number = input('请输入商品的数量: ')
    goods = [name, price, number]
    container.append(goods)
    answer = input('是否继续添加商品? (按q/Q退出)')
    if answer.lower() == "q":
        flag = False
for i in container:
    print(i)













