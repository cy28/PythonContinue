# 文件夹复制
# 封装成一个函数
import os


# 1. 源文件目录下只能是文件的情况
# def copy1(src1, target1):
#     if os.path.isdir(src1) and os.path.isdir(target1):
#         filelist = os.listdir(src1)  # 获取源目录下的文件和文件夹, 得到一个列表
#         for file in filelist:  # 遍历这个列表, 将目录名和文件名拼接, 得到一个完整的路径
#             path1 = os.path.join(src1, file)
#             with open(path1, 'rb') as r_stream:
#                 content = r_stream.read()  # 读一个完整路径里面的内容
#             path2 = os.path.join(target1, file)
#             with open(path2, 'wb') as w_stream:
#                 w_stream.write(content)
#         else:
#             print('复制完毕')
#
#
# copy('0.test_document', '0.copy_document')

# 2. 源文件目录下既有文件, 也有文件夹


def copy2(src2, target2):
    if os.path.isdir(src2) and os.path.isdir(target2):
        filelist = os.listdir(src2)                         # 获取传入的源目录下的文件和文件夹, 得到一个列表
        for file in filelist:
            path1 = os.path.join(src2, file)                # 遍历这个列表, 将源目录名和文件名拼接, 得到一个完整的路径
            if os.path.isdir(path1):                        # 判断得到的路径是一个目录还是一个文件
                target2_path = os.path.join(target2, file)  # 得到一个目标目录对应的应该存在的目录路径
                os.mkdir(target2_path)                      # 在目标目录中创建该目录
                copy2(path1, target2_path)                  # 新的源路径, 和目标路径, 进行递归
            else:
                with open(path1, 'rb') as r_stream:
                    content = r_stream.read()  # 读一个完整路径里面的内容
                path2 = os.path.join(target2, file)
                with open(path2, 'wb') as w_stream:
                    w_stream.write(content)
        else:
            print('复制完毕')


copy2('0.test2', '0.copy2')






































