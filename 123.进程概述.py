"""
进程是操作系统进行资源分配和调度的基本执行单位。

程序是指令,数据及其组织形式的描述, 进程是程序的实体

它代表了一个正在运行的程序实例，包含了程序代码、相关数据以及执行所需的系统资源。

进程在操作系统中独立运行，并拥有自己的内存空间、堆栈、文件描述符、寄存器等。

对于操作系统来说, 一个任务就是一个进程

"""


"""
并发（Concurrency）和并行（Parallelism）

并发指的是在同一时间段内处理多个任务的能力。在并发中，任务可以交替进行，通过时间片轮转或者优先级调度等方式，每个任务都能够得到一定的处理时间。尽管在任意时刻只有一个任务在执行，但是多个任务之间可以快速地切换，给人一种同时进行的感觉。并发的目标是提高系统的吞吐量和响应性，使得多个任务可以在有限的资源下共享资源并合理地协调。

并行指的是同时执行多个任务的能力。在并行中，多个任务可以同时进行，每个任务在不同的处理单元上独立地执行。并行的目标是加速任务的执行，通过同时利用多个处理单元（例如多个CPU核心）来提高计算性能。并行通常需要硬件的支持，例如多核处理器或者分布式系统。

"""






















