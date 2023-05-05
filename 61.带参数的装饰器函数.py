# 1. 如果是原函数需要单个参数

def decorator1(func):
    def wrapper1(adr):  # 那么这个位置, 也需要传个参数
        func(adr)      # 这个参数给到func
        print('精装修')
    return wrapper1


@decorator1
def house1(address):
    print(f'{address}是一个土胚房')


house1('四合院')

# 2. 如果原函数需要多个参数, 用*args


def decorator2(func):
    def wrapper2(*args):  # 那么这个位置, 也需要传个参数
        func(*args)      # 这个参数给到func
        print('精装修')
    return wrapper2


@decorator2
def house2(address, area, size):
    print(f'{address}是一个位于{area}的{size}平方米土胚房')


house2('四合院', '北京', 110)
# 四合院是一个位于北京的110平方米土胚房
# 精装修

# 3. 如果原函数有多个参数, 包括关键字参数, 用*args, **kwargs


def decorator3(func):
    def wrapper3(*args, **kwargs):
        func(*args, **kwargs)
        print('精装修')
    return wrapper3


@decorator3
def house3(address, area, size=110):
    print(f'{address}是一个位于{area}的{size}平方米土胚房')


house3('四合院',  size=40, area='北京')

# 四合院是一个位于北京的40平方米土胚房
# 精装修
















