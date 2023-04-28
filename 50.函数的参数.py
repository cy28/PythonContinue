# 1. 为什么函数需要设置参数

# 在之前的案例中, 随机生成4位验证码, 如果我想修改验证码的位数, 则需要传入参数来实现
import random


def generate_code(n):
    s = 'qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(n):
        r = random.choice(s)
        code += r
    print(code, end=' ')
    return code


generate_code(4)  # aL5e
print()
generate_code(6)  # ArDrPD
print()

"""
注意
    1. 定义函数时，传入的参数叫做形式参数，也叫作形参
    2. 调用函数时，传入的参数叫做实际参数，也叫作实参
    3，形参和实参的名字可以一致，因为本质上他们开辟的是不同的内存
    4. 调用时传入的参数默认与定义时的参数顺序一致
"""

# 2. 参数的分类


#   1 必须参数 传入参数的类型必须保持一致，而且数量必须匹配
def person(name, age):
    print('这个人的名字是%s，年龄是%d' % (name, age))


person('chen', 23)  # 这个人的名字是chen，年龄是23


#   2 关键字参数  使用关键字参数允许实参的顺序和形参不匹配

person(age=23, name="chen")  # 这个人的名字是chen，年龄是23

#   3 默认参数  定义函数时，给一个参数定义了默认值，后续不用给他传参，会使用默认值。也可以给他传参，这时候会覆盖掉默认值

# 默认参数一般放在参数列表的最后面，否则会报错
# 举例:
# 定义: def person(name, age, is_remember = True):
# 调用: person('chen', 23) 传两个参数就够了

# 3. 参数的数据类型可以是任意数据类型

# 举例: 参数的数据类型是列表

library = ['python精通', 'MySQL', '数据分析', '人工智能']


def add_book(books):  # 这里的books和library都指向同一片内存空间
    book_name = input('输入书籍名称: ')
    books.append(book_name)
    print('书籍添加成功')


def show_book(books):
    for i in books:
        print(i, end=" ")
    print()


add_book(library)  # 相当于books = library

show_book(library)










