# 猜拳游戏 三局两胜
import random
game_count = 0
person_v = 0
machine_v = 0

while game_count < 3:
    machine_num = random.randint(0, 2)
    person_num = int(input("请输入剪刀(0), 石头(1), 布条(2):"))

    if machine_num == person_num:
        print('本轮平局')
    elif (person_num == 0 and machine_num == 2) or (person_num == 1 and machine_num == 0) or (person_num == 2 and machine_num == 1):
        print('恭喜,这一回合你赢了')
        person_v += 1
    else:
        print('不好意思,这一回合电脑赢了')
        machine_v += 1
    game_count += 1

if person_v > machine_v:
    print('恭喜你取得了最后的胜利')
elif machine_v > person_num:
    print('不好意思, 你输了')
else:
    print('最后打平了')





















