# 在 Python 中，生成器对象除了使用 next() 方法逐个获取元素外，还可以使用 send() 方法向其发送一个值，并且在生成器函数中使用 yield 关键字来接收该值。
# 这种方式可以在生成器对象中传递信息，实现更加灵活的生成器。下面是一个简单的示例，其中定义了一个生成器函数 counter()，
# 用于生成一个无限序列，每次生成的元素为当前计数器的值，每次调用 next() 方法都会递增计数器。
# 此外，该生成器函数还定义了一个变量 delta，用于保存每次调用 send() 方法时传入的值，用于修改计数器的递增步长。


def gen():
    i = 0
    while i < 5:
        temp = yield i
        # 第一次send, return0, 然后暂停在这个位置
        print('temp: ', temp)
        i += 1
    return '没有更多数据'


g1 = gen()  # 1. 得到了生成器的地址

print(g1.send(None))  # 2. 先调用生成器函数, 执行yield i, 打印出一个0 并暂停在 temp = yield i 此时temp并没有接收到值
# 注意 第一次send None的原因是, 程序会被卡在yield i ,第一次的赋值语句并不会被执行
print(g1.send('hehe'))  # 3. 继续调用生成器函数, 执行temp = 被赋值hehe, 打印hehe i变1 继续执行到yield i, 打印出1, 然后暂停
print(g1.send('haha')) # 4. 调用函数, 执行赋值语句, temp 赋值haha 打印haha 然后打印2 卡住

# 0
# temp:  hehe
# 1
# temp:  haha
# 2

# 程序的执行流程
# 1. 定义一个名为gen()的生成器函数。
# 2. 调用gen()函数返回一个生成器对象g1。
# 3. 调用g1.send(None)，启动生成器的执行，并返回i的值0。
# 4. 调用g1.send('hehe')，生成器从yield语句恢复执行，temp变量被赋值为'hehe'，打印'temp: hehe'，并返回i的值1。
# 5. 调用g1.send('haha')，生成器从yield语句恢复执行，temp变量被赋值为'haha'，打印'temp: haha'，并返回i的值2。
# 6. 继续调用g1.send()，生成器继续执行，直到返回4。
# 7. 再次调用g1.send()时，生成器没有更多数据可返回，抛出StopIteration异常，被捕获并返回字符串'没有更多数据'。
# 8. 最后，该字符串被打印出来。



