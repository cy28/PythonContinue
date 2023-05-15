"""
在使用 re.match 函数时，可以使用起名的方式为正则表达式的各个部分命名，并通过命名的方式获取匹配结果。
这个功能通过在正则表达式的模式中使用 (?P<name>pattern) 的语法来实现

"""
import re

text = "John Doe, Age: 25, Email: johndoe@example.com"

pattern = r"(?P<name>\w+)\s+Doe, Age: (?P<age>\d+), Email: (?P<email>\w+@\w+\.\w+)"
match = re.match(pattern, text)

if match:
    name = match.group('name')
    age = match.group('age')
    email = match.group('email')
    print("Name:", name)
    print("Age:", age)
    print("Email:", email)

# Name: John
# Age: 25
# Email: johndoe@example.com
