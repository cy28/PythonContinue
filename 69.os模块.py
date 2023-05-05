"""
os-operating system
在Python中，"os"通常指的是操作系统模块（os module），是用于访问和管理操作系统功能的一个内置模块。
这个模块提供了许多与操作系统相关的函数和变量，使得Python程序可以直接与操作系统交互。

一些文件指令系统的缩写：

ls: 列出目录中的文件和子目录 (list)
cd: 切换当前工作目录 (change directory)
pwd: 显示当前工作目录的路径 (print working directory)
mkdir: 创建一个新目录 (make directory)
rmdir: 删除一个空目录 (remove directory)
cp: 复制文件或目录 (copy)
mv: 移动或重命名文件或目录 (move)
rm: 删除文件或目录 (remove)
touch: 创建一个新文件 (create a new empty file)
cat: 连接文件并打印到标准输出 (concatenate and print to standard output)
grep: 在文件中搜索指定的字符串 (global regular expression print)
chmod: 更改文件或目录的权限 (change mode)
chown: 更改文件或目录的所有者 (change owner)
ln: 创建一个链接 (link)

"""


import os

"""
os.path
os.path.dirname(__file__) 获取当前文件所在的文件目录(绝对路径)
os.path.join('原路径', '需要拼接的路径'), 返回一个拼接后的路径

"""

# 1. 获取当前路径
# print(os.curdir)  # current directory

"""
# 文件系统操作：
os.getcwd():            # 获取当前工作目录。  get current working directory

os.chdir(path):         # 改变当前工作目录。chdir是change directory的缩写，表示更改当前工作目录的意思。
                        # 在Python的os模块中，chdir是一个函数，它用于更改当前工作目录。
                        # 该函数接受一个字符串参数，表示要更改的目标工作目录的路径。

os.listdir(path):       # 获取指定目录下的所有文件和子目录的列表。
os.mkdir(path):         # 创建一个新目录。
os.rmdir(path):         # 删除一个目录。
os.rename(src, dst):    # 将文件或目录从src重命名为dst。
os.remove(path):        # 删除指定路径的文件。

# 进程管理：
os.fork():              # 创建一个新进程。
os.kill(pid, signal):   # 向指定进程发送指定信号。
os.getpid():            # 获取当前进程的PID。

# 环境变量：
os.getenv(key):         # 获取指定环境变量的值。
os.putenv(key, value):  # 设置指定环境变量的值。
3
# 其他：
os.system(command):     # 在命令行执行指定命令。
os.path.join(path, *paths): # 将多个路径组合成一个完整的路径。
os.path.exists(path):   # 检查指定路径是否存在。

"""

# 2. os.mkdir(path):         # 创建一个新目录。
"""
os.mkdir(path)是一个Python内置函数，用于创建一个新的目录。它接受一个字符串参数path，表示要创建的目录的路径。

具体来说，os.mkdir(path)会在指定路径下创建一个新目录，目录名为path所表示的字符串。如果目录已经存在，会抛出一个FileExistsError异常。

下面是一个示例：

# 创建一个名为"testdir"的新目录
os.mkdir("testdir")
上面的代码将在当前工作目录下创建一个名为"testdir"的新目录。

需要注意的是，如果路径中包含多级目录，那么os.mkdir只会创建最后一级目录，如果需要同时创建多级目录，可以使用os.makedirs函数。

"""

# 3. os.rmdir(path)        # 删除一个空目录。只能删除空目录, 如果目录不是空的, 就会报错
# os.rmdir('./testdir')      #./表示当前目录

# 4. rename() 重命名文件或者文件夹
# 两个参数 第一个参数：原来的名字 第二个参数：想要更改的名字
# os.rename('test.py', 'demo.py')

# 5. remove() 删除文件
# os.remove('demo.py')

# 6. 拼接路径 os.path.join(目录名, 扩展, 扩展, .......)
"""
os.path.join() 用于智能地连接一个或多个路径组件。它返回一个字符串，表示连接的路径组件。
第一个参数 path 是初始路径组件，所有后续的路径组件将与它连接。
*paths 参数用于传递一个或多个额外的路径组件。这些组件可以是字符串或其他路径样式的对象。
"""

result = os.path.join(os.getcwd(), 'file', 'test')  # E:\Code_Learning\PythonContinue\file\test
print(result)

# 7. 获取文件的大小 os.path.getsize('')  返回的单位是字节
print(os.path.getsize('1.变量命名.py'))  # 490

# 8. 判断是否是文件 os.path.isfile('')  返回True和False
print(os.path.isfile('1.变量命名.py'))  # True


# 9. 判断是否是文件夹 应该是在该文件夹所在目录进行查找
print(os.path.isdir('1.变量命名.py'))  # False

# # 10. 判断文件和文件夹是否存在
# print(os.path.exists('1.第一条python程序.py'))  # True

# 11. 获取文件名和后缀
name = r'E:\Code_Learning\PythonContinue\0.test_document\test3_70.jpg'

# 分割文件和前缀
result3 = os.path.split(name)
print(result3)  # ('E:\\Code_Learning\\PythonContinue\\0.test_document', 'test3_70.jpg')

# 分割文件和扩展名
result4 = os.path.splitext(name)
print(result4)  # ('E:\\Code_Learning\\PythonContinue\\0.test_document\\test3_70', '.jpg')


# 12. listdir() 返回指定目录下的所有的文件和文件夹, 返回保存到一个列表中
list1 = os.listdir('0.test_document')
print(list1)  # ['test1_66', 'test2_67', 'test3_70.jpg']

# 如何删除整个目录

"""
os.rmdir(path)              # 删除一个目录。只能删除空目录, 如果目录不是空的, 就会报错
os.rmdir('./testdir')       #./表示当前目录

remove() 删除文件
os.remove('demo.py')
"""

# path1 = r'E:\Code_Learning\PythonContinue\0.test_document'
#
# filelist = os.listdir(path1)  # ['test1_66', 'test2_67', 'test3_70.jpg']
#
# for file in filelist:
#     path1 = os.path.join(path1, file)
#     os.remove(path1)
# else:
#     os.rmdir(path1)  # 目录里面的文件删完了, 再删整个目录

