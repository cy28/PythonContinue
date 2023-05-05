# 文件复制
# open只能操作文件, 不能操作文件夹
"""
原文件: c:\p1\girl.jpg
目标文件: c:\p2\girl.jpg
流程:
    1. 得到content
    2. 给到目标地址, 用write把content读进去

with 结合open使用, 可以帮我们自动释放资源


with open('c:\p1\girl.jpg', 'rb') as r_stream:
    content = r_stream.read()  # 读取文件的内容

with open('c:\p2\girl.jpg', 'wb') as w_stream:
    w_stream.write(content)

"""

















