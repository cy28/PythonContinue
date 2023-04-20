"""
需求：
1. 模拟超市付款 ： 商品单价  商品数量
2. 键盘上输入商品单价和商品的数量
3. 计算付款总额 数据类型为float
4. 提示顾客有四种付款方式 不同的付款方式有不同的折扣
    现金      没有折扣
    微信      0.95折
    支付宝     给与鼓励金,是付款金额的10%, 可直接折算到付款金额中
    刷卡      满100-20
"""
import random
total = 0  # 定义当前的消费金额

while True:
    number = random.randint(0, 10000)
    money = random.uniform(0, 10000)
    total += number * money
    print("此时的消费金额为%.2f" % total, "是否继续购买?")
    answer = input("按任意键继续/按q退出:")
    if answer == 'q':
        break
print("你的消费金额为%.2f" % total)



















































