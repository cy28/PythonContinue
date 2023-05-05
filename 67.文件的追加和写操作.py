# 1. w模式

# 注意:
#   write() 每次进行写操作, 就会把文件中的内容先清除, 再写入内容
#   writelines(iterable) 添加一个可迭代对象, 但是并没有换行效果, 需要自己加\n

f = open('0.test_document/test2_67', 'w', encoding='utf-8')  # mode = 'w' 会把原来文件中的内容全部替换

s = """你好, 欢迎来到澳门赌场!
赠送您一个金币!"""

result = f.write(s)

print(result)  # 22 写入的字符个数

f.write('龙五')  # 每次写入的时候, 同一个流(f.close之前的), 都会接着上一次写过的地方接着写

f.writelines(['赌神高进', '赌侠小刀\n', '赌圣周星星'])  # 如果要换行, 得自己加\n

f.close()  # 资源释放后, 无法继续对流进行操作

# 2. a模式 append 追加
f = open('0.test_document/test2_67', 'a')         # 'a'已追加的方式向原文添加内容，不会影响原文件的内容

f.write('这是追加的内容')

f.close()


































