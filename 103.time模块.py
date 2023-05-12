"""
time模块是Python标准库中的一个模块，主要用于获取和处理时间。
通过time模块，我们可以获取当前的时间、计算时间间隔、格式化时间等。

下面是一些常用的time模块函数：

time.time(): 返回当前时间的时间戳，即从1970年1月1日零时零分零秒起到现在的秒数。
time.localtime([secs]): 将一个时间戳转换为本地时间，如果不传入参数则返回当前时间。
time.sleep(secs): 让程序休眠secs秒。
time.strftime(format[, t]): 格式化时间，将时间格式化成指定格式的字符串。第二个参数t是可选的，如果不传入则默认使用本地时间。
time.strptime(string[, format]): 将一个字符串解析为时间元组，第二个参数format是可选的，

除了上述常用函数外，time模块还有其他一些函数，如：
time.gmtime([secs]): 将一个时间戳转换为UTC时间。
time.asctime([t]): 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2018"（格式化后的）时间字符串。
time.ctime([secs]): 接受时间戳并返回一个可读的形式为"Tue Dec 11 18:07:14 2018"（格式化后的）时间字符串。
time.perf_counter(): 返回一个CPU级别的精确时间计数值，用于性能测试。

"""

import time

# 1. time.time() 获取当前时间戳 即从1970年1月1日零时零分零秒起到现在的秒数。
timestamp = time.time()
print("当前时间戳为：", timestamp)   # 当前时间戳为： 1657651467.6840398

# 2. time.ctime([secs]) 接受时间戳并返回一个可读的形式为"Tue Dec 11 18:07:14 2018"（格式化后的）时间字符串。
print(time.ctime(time.time()))  # Fri May 12 09:56:14 2023

# 3. time.localtime([secs]) 将时间戳转换为本地时间元组，如果不传入参数则返回当前时间。
local_time = time.localtime(timestamp)
print("本地时间为：", local_time)
# 本地时间为： time.struct_time(tm_year=2023, tm_mon=5, tm_mday=12, tm_hour=9, tm_min=56, tm_sec=14, tm_wday=4, tm_yday=132, tm_isdst=0)
# tm_wday=4 表示周几 0-6 表示 4表示周五
# tm是time的缩写
# tm_wday: 星期几（0 表示星期一，6 表示星期日）
# tm_yday: 年份中的第几天（1 到 366）
# tm_isdst: 夏令时标志（-1、0 或 1，-1 表示夏令时信息不可用）

# 4. time.mktime 函数接受一个时间元组作为参数，将其转换为对应的时间戳, 但是会去掉小数点后面的精度
time_tuple = time.struct_time((2023, 5, 12, 9, 56, 14, 4, 132, 0))
print(time.mktime(time_tuple))  # 1683856574.0

# 5. time.sleep(secs): 让程序休眠secs秒。休眠5秒
print("开始休眠")
time.sleep(5)
print("休眠结束")

# 6. time.strftime(format[, t]) 将时间元组格式化成字符串 将时间格式化成指定格式的字符串。第二个参数t是可选的，如果不传入则默认使用本地时间。
# strftime 是 "string format time" 的缩写，表示将时间格式化为字符串的操作。

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("格式化后的时间为：", formatted_time)   # 格式化后的时间为： 2022-07-12 17:17:47

# %Y：表示四位数的年份，例如：2023
# %m：表示两位数的月份，范围为01到12
# %d：表示两位数的日期，范围为01到31
# %H：表示两位数的小时，范围为00到23
# %M：表示两位数的分钟，范围为00到59
# %S：表示两位数的秒数，范围为00到59

# 7. time.strptime(string[, format]): 将一个字符串解析为时间元组，第二个参数format是可选的，
# string parse time"，用于将字符串解析成时间格式，

time_str = "2023-04-12 10:30:00"
parsed_time = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
print("解析后的时间为：", parsed_time)
# 解析后的时间为： time.struct_time(tm_year=2023, tm_mon=4, tm_mday=12, tm_hour=10, tm_min=30, tm_sec=0, tm_wday=2, tm_yday=102, tm_isdst=-1)
