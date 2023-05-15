# datetime 模块是 Python 标准库中的一个模块，用于处理日期和时间相关的操作。
# 它提供了各种类和函数，用于创建、操作和格式化日期时间对象，并进行日期时间计算、比较和格式化。

"""
下面是 datetime 模块中一些常用的类和函数：

datetime 类：表示日期和时间的对象。它可以表示年、月、日、时、分、秒和微秒，并提供了各种方法用于操作和格式化日期时间。
date 类：表示日期的对象。它包含年、月和日，并提供了方法用于日期的计算、比较和格式化。
time 类：表示时间的对象。它包含时、分、秒和微秒，并提供了方法用于时间的计算、比较和格式化。
timedelta 类：表示时间间隔的对象。它可以表示一段时间的差异，如天数、秒数、微秒数等，用于日期时间的加减操作和计算。
strftime() 函数：用于将日期时间对象格式化为字符串。
strptime() 函数：用于将字符串解析为日期时间对象。
today() 函数：返回当前日期的 datetime 对象。
now() 函数：返回当前日期和时间的 datetime 对象。
utcnow() 函数：返回当前的 UTC 日期和时间的 datetime 对象

"""

import datetime

# 1. datetime.datetime.now() 获取当前日期和时间
current_datetime = datetime.datetime.now()
print("当前日期和时间:", current_datetime)
# 当前日期和时间: 2023-05-12 10:46:23.496104

# 2. datetime.datetime() 创建一个特定的日期和时间
specific_datetime = datetime.datetime(2023, 5, 12, 10, 30, 0)
print("特定日期和时间:", specific_datetime)
# 特定日期和时间: 2023-05-12 10:30:00

# 3. 获取日期和时间的各个部分
year = specific_datetime.year
month = specific_datetime.month
day = specific_datetime.day
hour = specific_datetime.hour
minute = specific_datetime.minute
second = specific_datetime.second
print("年:", year)
print("月:", month)
print("日:", day)
print("时:", hour)
print("分:", minute)
print("秒:", second)

# 4. .strftime() 相当于对象的方法, 格式化日期和时间为字符串
formatted_datetime = specific_datetime.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后的日期和时间:", formatted_datetime)
# 格式化后的日期和时间: 2023-05-12 10:30:00

# 5. .strptime() 解析字符串为日期和时间
parsed_datetime = datetime.datetime.strptime("2023-05-12 10:30:00", "%Y-%m-%d %H:%M:%S")
print("解析后的日期和时间:", parsed_datetime)

# 6. 执行日期和时间运算
future_datetime = specific_datetime + datetime.timedelta(days=7)
print("未来日期和时间:", future_datetime)

# 7. 比较日期和时间
is_future = future_datetime > current_datetime
print("是否是未来时间:", is_future)





















