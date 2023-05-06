# 进程 >> 线程 >> 协程

def task1(n):
    for i in range (n):
        print(f'正在搬第{i}块砖')
        yield None


def task2(n):
    for i in range (n):
        print(f'正在听第{i}首歌')
        yield None


g1 = task1(5)
g2 = task2(5)

while True:
    try:
        next(g1)
        next(g2)
    except:
        pass

# 正在搬第0块砖
# 正在听第0首歌
# 正在搬第1块砖
# 正在听第1首歌
# 正在搬第2块砖
# 正在听第2首歌
# 正在搬第3块砖
# 正在听第3首歌
# 正在搬第4块砖
# 正在听第4首歌

















