"""
在Python中，json模块是用于处理JSON（JavaScript Object Notation）数据的标准库模块。

JSON的中文意思是“JavaScript对象表示法”。JSON最初是由JavaScript语言的创造者Douglas Crockford提出的一种数据交换格式，并得到了广泛的应用。
尽管JSON名称中包含“JavaScript”，但它已经成为一种独立于编程语言的通用数据格式，并且在许多不同的编程语言中都有对应的解析和生成器库。
因此，尽管JSON的名称中含有“JavaScript”，但它与JavaScript语言并没有直接的依赖关系，可以在许多编程语言和环境中使用。

JSON是一种轻量级的数据交换格式，常用于将数据从一个应用程序传输到另一个应用程序，或将数据存储在文件中。
用于跨语言系统的数据传输

json模块提供了一组函数和类，用于在Python中解析和生成JSON数据。以下是json模块的一些主要功能和用法：

"""
import json

# 1. Python数据类型与json格式的相互转化

# a.  数据类型-->json, 一般称为序列化
# 编码为JSON字符串
data = {'name': 'John', 'age': 30}
json_str = json.dumps(data)
print(json_str)  # 输出: {"name": "John", "age": 30}


# b.  json-->python的数据类型, 一般称为反序列化
# 解码为Python对象
json_data = '{"name": "John", "age": 30}'
obj = json.loads(json_data)
print(obj['name'])  # 输出: John


# 2. python数据类型转化为json格式, 对数据类型是要有要求的, 默认只支持

"""
python                  josn

dict                    object
list, tuple             array
str                     string
int float               number
True                    true
False                   false
None                    null

其他类型, 需要自定义JSONEncoder才能实现
"""

















