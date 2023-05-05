# 在Python中，我们使用内置的open()函数来打开文件并读取或写入数据。该函数的语法如下：

# open(file, mode='r', buffering=-1, encoding=None)

"""
参数说明：

1. file：要打开的文件名（包括路径）或文件对象。
2. mode：打开文件的模式，如下：
'r'：只读模式（默认值）。
'w'：写入模式，每次写入前会清空文件。
'a'：追加模式，不清空文件，在文件末尾添加新内容。
'x'：独占创建模式，只有文件不存在时才会创建文件，否则会抛出异常。
'b'：二进制模式，与其他模式结合使用，如'rb'，'wb'，'ab'，'xb'等。
't'：文本模式（默认值），与其他模式结合使用，如'rt'，'wt'，'at'，'xt'等。

mode的参数默认为rt
"""

# 1. 我们想读取一个文件中的内容
# open函数其返回值是一个stream. 用f变量去接这个流, 相当于open函数在pycharm和磁盘中的文件建立了一个链路, 用f1为这个链路命名
# 新建文档的默认编码方式为gbk, 而python默认的解码方式是utf-8, 所以我们要把编码方式设为utf-8
# 读文件的时候, 给文件一个名字
f1 = open('0.test_document/test1_66', 'r', encoding='utf-8')


# a. read() 一字节一字节的读, 把所有的内容读完
# content = f1.read()  # 从这个链路中去读东西
# print(content)
# hello 第66个python文件
# helloworld

# b. readable()  是否可读
# content1 = f1.readable()
# print(content1)  # True

# c. readline()  只能读一行
# 注意 由于上面的read方法已经将流中的内容读完了, 如果前面不注释掉, 这里就什么都读不出来
# print(f1.readline())  # hello 第66个python文件

# d. readlines()也是按行读，但是会读所有行，并以一个列表的形式返回，列表中的每一个元素就是文件中的一行
# 同理, 流中内容读完就没有了, 如果c不注释掉, 这里就只会读出第二行的内容
print(f1.readlines())  # ['hello 第66个python文件\n', 'helloworld']

# 如果读图片, 则mode应该改为rb 读二进制的模式



















