# 模块的本质是一个python文件
# 根据自身项目需求写的一些文件，就是自定义模块
# 自定义模块同样通过import导入
# 导入自定义模块后就可以直接使用里面的变量和函数

import sys
sys.path.append('.\98_1_1.自定义模块')


# 1. 直接导入
# 导入名为“my_module”的自定义模块
import my_module1

# 将“greeting”变量的值从“Hello, ”更改为“Hi, ”
my_module1.greeting = "Hi, "

# 定义一个名为“name”的变量，其值为“Alice”
name = "Alice"

# 使用“my_module.greet”函数向“name”参数传递“Alice”值，并在控制台上打印问候语
my_module1.greet(name)  # Hi, Alice!

# 2. 通过通配符*导入
# from my_module import *

# 3. 精确导入，精确导入模块中的变量和方法
# from my_module import greeting


# 注意:
# 无论是import 还是from的形式, 都会将模块的内容进行加载
# 如果不希望模块加载的时候, 调用里面的函数, 就会用到__name__








