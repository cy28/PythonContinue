"""
需求:
1. 产生一个随机数,进行猜测
2. 可以猜多次,直到猜对停止猜测
3. 如果猜错了,给出适当的提示,猜大了还是猜小了
4. 统计到猜对一共猜了几次
5. 1次就中,运气太好了,去买彩票吧
    2-5次 运气还可以啊
    6次以上 运气一般a
"""

import random
count = 0
num1 = random.randint(1, 50)

while True:
    num2 = int(input("在此处输入你的猜测:"))
    count += 1
    if num1 == num2:
        print('恭喜你猜对了!')
        break
    elif num1 > num2:
        print("你猜小了,请重新输入")
    else:
        print("你猜大了,请重新输入")
print('你一共猜了%d次' % count)
if count == 1:
    print('运气太好了,去买彩票吧')
elif 2 <= count <= 5:
    print('运气还可以啊')
else:
    print('运气一般哟')














