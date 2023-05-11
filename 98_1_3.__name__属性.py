"""
在 Python 中，每个模块都有一个特殊的属性 __name__。该属性返回一个字符串，表示当前模块的名称。

当一个模块被直接运行时，它的 __name__ 属性被设置为字符串 "__main__"。

换句话说，如果一个 Python 脚本被作为主程序直接运行，那么该脚本所对应的模块的 __name__ 属性将会被自动设置为 "__main__"。

而当该python文件被当做模块导入其他的python文件中时, 此时的__name__就等于模块的名称

"""

import sys
sys.path.append('.\98_1_1.自定义模块')

import my_module3 as m3

print(m3.add(1, 2))


print(dir(m3))
# ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'add', 'subtract']

print(m3.__name__)  # my_module3

# 在导入文件中, 模块的__name__由模块中的__main__变为了模块名my_module3
# 因此此时模块中的if __name__ = __mian__不成立, 因此测试代码不会被执行





