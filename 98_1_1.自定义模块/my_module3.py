def add(x, y):
    return x + y


def subtract(x ,y):
    return x - y

# 现在想检查一下写的函数能否正常运行, 如果在导入模块的到文件中调用, 就会显得很麻烦
# 于是采用以下方式测试代码


print(__name__)  # __main__  在模块自身中, __name__就是__main__

if __name__ == '__main__':
    print(add(1, 2))
    print(subtract(1, 2))















