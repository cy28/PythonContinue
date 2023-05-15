import datetime

"""
datetime 类：表示日期和时间的对象。它可以表示年、月、日、时、分、秒和微秒，并提供了各种方法用于操作和格式化日期时间。
date 类：表示日期的对象。它包含年、月和日，并提供了方法用于日期的计算、比较和格式化。
time 类：表示时间的对象。它包含时、分、秒和微秒，并提供了方法用于时间的计算、比较和格式化。
timedelta 类：表示时间间隔的对象。它可以表示一段时间的差异，如天数、秒数、微秒数等，用于日期时间的加减操作和计算。

"""

print(datetime.time.hour)  # <attribute 'hour' of 'datetime.time' objects>

print(datetime.date.day)   # <attribute 'day' of 'datetime.date' objects>

# 创建date对象
d1 = datetime.date(2023, 5, 11)

print(datetime.date.ctime(d1))  # Fri May 11 00:00:00 2023
print(d1.day)  # 11

# 返回的是当前的日期, 不需要构造类
print(datetime.date.today())  # 2023-05-12


# 时间差
time_delta = datetime.timedelta(hours=2)
print(time_delta)  # 2:00:00

now = datetime.datetime.now()
print(now)  # 2023-05-12 11:18:46.482731

result = now + time_delta
print(result)  # 2023-05-12 13:19:52.952296



