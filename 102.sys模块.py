"""
sys 模块是 Python 标准库中的一个内置模块，提供了与 Python 解释器及系统交互相关的功能。通过 import sys 语句可以导入该模块进行使用。

sys 模块提供了一些函数和变量，用于获取和操作与 Python 解释器及系统相关的信息。下面是一些常用的 sys 模块的函数和变量：

sys.exit([arg])：用于退出 Python 解释器。可选参数 arg 可以用作退出状态码，默认为零。

sys.modules：是一个字典，包含已导入模块的缓存。在该字典中，键是模块名，值是模块对象。

sys.platform：是一个字符串，表示当前运行 Python 解释器的平台。例如，"win32" 表示 Windows 平台，"linux" 表示 Linux 平台。

sys.stdin、sys.stdout、sys.stderr：分别表示标准输入、标准输出和标准错误输出的文件对象。可以通过这些对象进行输入输出操作。

除了上述常用的函数和变量之外，sys 模块还提供了其他一些功能，如处理系统级别的异常、控制垃圾回收机制、获取 Python 解释器的版本信息等。

总的来说，sys 模块提供了与 Python 解释器及系统交互的功能，可以方便地获取和操作与系统相关的信息，对于系统级别的操作和配置非常有用。

"""


import sys

# 1. sys.argv
# argv 是 "argument vector" 的缩写，表示命令行参数向量。在计算机科学中，"向量" 指的是一组按照顺序排列的元素
# 是一个包含命令行参数的列表。当 Python 脚本被执行时，该列表会包含传递给脚本的命令行参数。

print(sys.argv)  # ['E:\\Code_Learning\\PythonContinue\\102.sys模块.py']


# 2. sys.path
# 是一个列表，包含解释器用于查找模块的路径。可以通过修改该列表来添加或修改模块搜索路径。

print(sys.path)
# ['E:\\Code_Learning\\PythonContinue', 'E:\\Code_Learning\\PythonContinue', 'E:\\Code_Learning\\PythonLearning', 'D:\\PyCharm 2022.3.2\\plugins\\python\\helpers\\pycharm_display', 'D:\\Python 3.10.9\\python310.zip', 'D:\\Python 3.10.9\\DLLs', 'D:\\Python 3.10.9\\lib', 'D:\\Python 3.10.9', 'D:\\Python 3.10.9\\lib\\site-packages', 'D:\\PyCharm 2022.3.2\\plugins\\python\\helpers\\pycharm_matplotlib_backend']

# sys.version
# 通过访问 sys.version，可以获取一个描述当前 Python 解释器版本的字符串。该字符串通常包含了 Python 版本号以及其他与版本相关的信息。

print(sys.version)
# 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)]









