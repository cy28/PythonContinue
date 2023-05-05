import os
# 判断是否是相对路径
result1 = os.path.isabs("E:/WebLearning/test2.jpg")  # 绝对路径

# 文件夹和文件同级的情况下, 可以直接通过文件夹名访问文件夹
result2 = os.path.isabs('0.test_document/test3_70.jpg')  # 相对路径

# ../表示跳到当前文件的上级目录

# 获取当前文件的绝对路径
path1 = os.path.abspath(__file__)
print(path1)  # E:\Code_Learning\PythonContinue\70.相对路径和绝对路径.py

# 获取当前文件的文件夹所在的绝对路径
path2 = os.getcwd()
print(path2)  # E:\Code_Learning\PythonContinue







