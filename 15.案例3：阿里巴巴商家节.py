"""
需求：
阿里巴巴商家节

1. 用户名，消费总金额， 账户系统， 优惠券
2. 如果消费金额在0-500，账户等级是lv1
   如果消费金额在500-200，账户等级是lv2
   如果消费金额大于2000，账户等级是lv3
3. lv1：随机赠送三张1-10元的优惠券
   lv2：赠送两张50元的优惠券，如果充值则送充值金额的10%
   lv3：赠送两张100元的优惠券，如果充值则送充值金额的15%

"""
import random
username = '世龙'
total = 1500  # 消费金额
money = 0     # 账户余额
coupon = 0    # 优惠券金额


if 0 < total < 500:   # lv1
    # 随机赠送3张1-10元的优惠券
    quan1 = random.randint(1, 10)
    quan2 = random.randint(1, 10)
    quan3 = random.randint(1, 10)
    # 将优惠券金额添加到
    coupon = quan1 + quan2 + quan3
elif 500 <= total <= 2000:
    coupon += 2*50
    recharge = input('%s, 是否充值，如果充值将返回金额的10%？(y/n)：')
    if recharge == 'y':
        money += 1.1*int(input('请输入你要充值的金额：'))
elif total > 2000:
    coupon += 2*100
    recharge = input('%s, 是否充值，如果充值将返回金额的15%？(y/n)')
    if recharge == 'y':
        money += 1.15*int(input('请输入你要充值的金额：'))

print('您当前的账户金额为%.2f, 当前的优惠券金额为%.2f' % (money, coupon))

















