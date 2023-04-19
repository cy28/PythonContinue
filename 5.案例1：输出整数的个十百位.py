number = int(input('请输入一个四位整数：'))

print('该整数的个位是：', number % 10)

print('该整数的十位是：', (number // 10) % 10)

print('该整数的百位是：', (number // 100) % 10)

print('该整数的千位是：', number // 1000)











