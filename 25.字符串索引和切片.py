"""
1. 下标：也叫索引(index)，表示字符串中的第几个数据

下标有两套索引机制:
1. 从左到右 从0开始
2. 从右到左 从-1开始

str1 = "welcome"
print(str1[3])   # c
print(str1[-2])  # m

"""

"""
2. 切片：从字符串中复制一段指定内容，生成一个新的字符串

切片的语法：
    字符串[start:end:step]  左闭右开
    start 表示开始下标，包含该下标对应的值
    end 表示结束下标，不包含改下标对应的值
    step 表示截取的步长，默认值为1  符号表示方向 为正数从左往右 为负数从右往左

"""

str2 = "welcome"
print(str2[0:3])          # wel      012              包含start，不包含end
print(str2[1:])           # elcome   123456           从start开始，一直截取到结束
print(str2[:4])           # welc     0123             从开始一直截取到结束
print(str2[-3:])          # ome      -3-2-1           从-3开始,到结尾
print(str2[1:4:2])        # ec       13               从1开始，隔两个步长截取
# print(str2[1:4:0])      # ValueError: slice step cannot be zero 步长不能为0
print(str2[::])           # welcome                   如果所有参数都不指定，则表示截取整个字符串
print(str2[::-1])         # emoclew                   表示翻转字符串
print(str2[-3:-1])        # om
print(str2[1:-1])         # elcom                     要中间,不要两头

