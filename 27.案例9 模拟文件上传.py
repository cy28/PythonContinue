"""
需求:
1. 模拟图片文件的上传 键盘上输入上传文件的名称包括扩展名,
2. 判断文件名称是否大于6位以上
3. 文件的扩展名是否是: jpg, png, gif格式, 如果不是则提示上传失败
4. 如果名字不满足条件, 而扩展名满足条件,则随机生成一个6位数字组成的文件名, 打印成功上传xxxxx.png
"""
import random
filename = input("请输入文件的名字:")
if filename.endswith("jpg") or filename.endswith("png") or filename.endswith("gif"):
    s = filename.rfind(".")
    name = filename[: s]
    if len(name) < 6:
        print('文件命名不符合要求, 已经重新命名')
        newname = random.randint(100000, 999999)
        new_filename = str(newname) + filename[s:]
        print("成功上传%s文件" % new_filename)
    else:
        print("成功上传%s文件" % filename)
else:
    print('文件格式错误, 文件上传失败')































