import multiprocessing


# 定义一个进程要执行的任务
def task():
    print("This is a child process.")


if __name__ == '__main__':
    # 创建一个进程对象
    process = multiprocessing.Process(target=task)

    # 启动进程
    process.start()

    # 等待进程执行完毕
    process.join()

    print("This is the main process.")
