"""
需求:
1. 两个骰子 1-6
2. 参与一局游戏, 赠送金币一枚
3. 充值获取金币, 10元20枚金币, 充值金额必须是10的倍数
4. 参与一局游戏, 消耗10枚金币
5. 猜大小,答对奖励两枚金币, 猜错没有奖励, 大于6点则为大,其余为小
6. 游戏结束条件: 1. 主动退出 2. 金币金额不足再参加游戏
7. 退出后,打印游戏局数, 同时打印当前金币数量

"""
import random
coins = 0  # 定义金币数
count = 0  # 定义游戏局数

if 5 > coins:
    answer = input("金币不足, 请充值! 任意键充值或q退出:")
    if answer == "q":
        exit()
    else:
        while True:
            money = int(input('请输入充值的金额: '))
            if money % 10 == 0:
                coins = money // 10 * 20
                print('充值成功! 当前的金币数为%d!' % coins)
                # 这里开始进行游戏
                answer1 = input("是否开始游戏(y/n):")
                if answer1 == "n":
                    exit()
                else:
                    while True:
                        while coins > 10 and answer1 == "y":
                            print('.....................开始游戏............................')
                            coins -= 10  # 游戏消耗金币
                            coins += 1  # 游戏赠送金币
                            count += 1
                            # 产生两个随机骰子数
                            ran1 = random.randint(1, 6)
                            ran2 = random.randint(1, 6)
                            guess = input("重置完毕, 请猜大小:")
                            # 判断是否猜对
                            if guess == "大" and ran1 + ran2 > 6 or guess == "小" and ran1 + ran2 <= 6:
                                coins += 2
                                print("恭喜你猜对了! 当前的金币数为%d" % coins)
                            else:
                                print("你猜错了! 当前的金币数为%d" % coins)
                            print("游戏局数为%d, 剩余金币为%d" % (count, coins))
                            answer1 = input("是否继续游戏(y/n): ")

                break
            else:
                print('充值失败, 不是10的倍数!')




















