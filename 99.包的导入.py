# python中包和文件夹的区别

"""
在Python中，包（Package）和文件夹（Folder）是两个相关但不完全相同的概念。

**包（Package）**是一个包含模块（Module）和其他子包的特殊文件夹。它允许组织和管理相关的模块，使得代码更加模块化和可重用。

一个包必须包含一个名为__init__.py的特殊文件，它可以为空文件，但它的存在告诉Python这是一个包。包的层次结构可以是多层次的，就像文件夹的嵌套结构一样。

"""

# 1. 通过包名导入module

from user_99 import module  # 可以通过包导入模块

u1 = module.User('admin', 123)

u1.show()  # admin 123


# 2. 通过包名.模块导入其中的方法

from user_99.module import User

u2 = User('admin2', 134)


# 3. 从另一包导入同名模块

from article_99 import module

a1 = module.Article('三国', '吴承恩')

a1.show()  # 发表文章名为三国的作者是吴承恩

# 4. 总结
# from 包 import 模块
# from 包.模块 import 类/函数/变量
# from 包.模块 import *


# 5. 即使两个模块在同一个包中, 导入也要向上面那样完整的导入

# 6. 搜索都是基于项目进行搜索









