"""
停车计费系统需求:
    1. 进入停车场, 记录进入时间, 出去停车场, 记录出去时间, 停车时间 = 出去时间-进入时间
    2. 停车场得到的数据结构是[{'车牌':[进入时间,出去时间]}, {'车牌':[进入时间,出去时间]}, {'车牌':[进入时间,出去时间]}
    3. 15分钟1块钱, 一个小时4块钱
    4. 停车场变量----> 全局变量

"""
import random
# 1. 定义一个停车场变量
parkinglot = []

# 2. 定义车辆进入函数
def enter():
    print('欢迎进入xxx停车场')
    number = input('输入车牌号: ')
    # 构建一辆车的数据结构 先定义一个空字典
    car = {}
    # number值作为key, 且进入时间我们默认为0, 用随机数产生一个离开的时间, 同时number键对应的值是一个列表
    car[number] = [0]  # number键的值是一个列表
    # 添加到parkinglot中
    parkinglot.append(car)  # 在parkinglot列表中, 每次添加的是一个字典
    print(f'{number}已进入停车场')

# 3. 定义车辆出去函数
def exit_1():
    print('欢迎下次光临本停车场')
    number = input('输入车牌号: ')
    for i in parkinglot:
        if number in i.keys():  # in 默认是跟字典的键进行比较, 这里可以直接写i
            exit_time = random.randint(0, 24)
            # 得到number后面的列表
            time_record = i.get(number)
            # 将退出时间加到这个时间记录中
            time_record.append(exit_time)
            # 计算花费
            cost = exit_time * 4
            print(f'{number}停车{exit_time}小时, 总共花费{cost}元')
            break
    else:  # 扫描number是否在键值中, 在就会被打断, 不在就会一直扫描未被打断, 进入else
        print('此车未在停车场中')


enter()
exit_1()


















