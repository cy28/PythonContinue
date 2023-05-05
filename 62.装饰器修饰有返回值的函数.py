# 原函数有返回值, 装饰器函数也必须有返回值, 而具体返回值是多少,根据实际情况而定

def decorator(func):
    def wrapper():
        m = func()
        print(f'原始花费{m}元')
        print('精装修')
        return 100000
    return wrapper


@decorator
def house():
    print('土胚房')
    return 50000


r = house()
print(r)


























