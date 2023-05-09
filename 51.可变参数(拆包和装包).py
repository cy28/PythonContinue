"""
可变参数:
    *args      一颗*  接收多个参数，会把所有的参数放在一个元组中
    **kwargs   两颗*  用来接收多个关键字参数(x = 'haha')，得到一个字典，在传输参数时，以key=value的形式传输
"""

# 1. 为什么出现了可变参数的形式
"""
在下面的实例中, 当我们算多个数求和的时候, 这里的形参的个数就不能写死了, 于是引入了可变参数的概念

# 求和
def get_sum(a, b):
    r = a + b
    print(r)
    
"""


def get_sum(*args):
    sum1 = 0
    for i in args:  # 要使用这个args, 就遍历这个元组
        sum1 += i
    print(sum1)


get_sum(1, 2, 3, 4)  # 10

# 2. 一颗* *args    形式 (* + 一个变量名) 名字可以随便取, 一般写成args(arguments)

# def get(*args):
#     print(args)
# get(1, 2, 3)  # (1, 2, 3) 打印出来的是元组

# 封装成元组是因为, 当参数传入时, 我们希望函数体不会改变参数

# 3. 说明 *会将参数打包在一起, 赋值时打包成列表, 函数参数打包成元组

*a, b, c = 1, 2, 3, 4, 5
print(a)  # [1, 2, 3]
print(b)  # 4
print(c)  # 5

a, *b, c = 1, 2, 3, 4, 5
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5

a, b, *c = 1, 2, 3, 4, 5
print(a)  # 1
print(b)  # 2
print(c)  # [3, 4, 5]


# 4. 拆包和装包

# 1. 函数定义时, 用*args 接受参数, 传入的参数是分散的, 会将所有的参数打包成一个元组

# 2. 函数调用时, 给参数加*, 会把这个传入的整体进行拆分

def get_sum2(*args):
    print(args)
    sum2 = 0
    for i in args:
        sum2 += i
    print(sum2)


list2 = [1, 2, 3, 4]

# get_sum2(list2)  # 报错 args == ([1, 2, 3, 4],)

get_sum2(*list2)  # 传入的参数是一个整体 加*进行拆包

# 5. 两颗*  **kwargs 里面存的是字典类型的参数 调用的时候必须传递关键字参数, 才能将其转化为key:value的形式


def book_name(**kwargs):
    print(kwargs)  # {'书名': '西游记', '作者': '吴承恩'}


book_name(书名='西游记', 作者='吴承恩')


# 同样 当传入的数据是一个字典时, 通过**进行拆分

book1 = {'书名': '红楼梦', '作者': '曹雪芹', '数量': 12}


def show(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


show(**book1)  # 相当于拆成 书名='红楼梦', 作者='曹雪芹', '数量'=12, 之后在函数中重新组装成一个字典

# 书名 红楼梦
# 作者 曹雪芹
# 数量 12

