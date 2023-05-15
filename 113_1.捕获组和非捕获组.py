"""
在正则表达式中，括号 () 用于创建捕获组（capturing group）或非捕获组（non-capturing group）。它们在正则表达式中有以下用途：

捕获组（Capturing Group）：括号内的模式被视为一个整体，并被捕获以供进一步处理或引用。

(pattern)：将括号内的模式作为一个捕获组。匹配该模式后，可以通过索引或特殊变量来引用捕获的内容。
示例：(\d{2})-(\d{2})-(\d{4}) 可以用于匹配日期格式，如 "01-25-2023"，并捕获年、月、日的信息。
非捕获组（Non-Capturing Group）：括号内的模式被视为一个整体，但不会被单独捕获和存储。

(?:pattern)：将括号内的模式作为一个非捕获组，用于分组但不需要捕获结果。
示例：(?:https?://)?(www\.\w+\.\w+) 可以用于匹配网址，并非捕获 http:// 或 https://，只捕获并存储 www.example.com。
分组的其他用途：括号还可以用于控制模式的分组、优先级和应用修饰符等。

(pattern1|pattern2)：在括号内使用 | 来表示或逻辑，匹配 pattern1 或 pattern2 中的任意一个。
(?=pattern) 和 (?!pattern)：用于正向预查和负向预查，括号内的模式将作为条件来匹配，但不会被包含在结果中。
需要注意的是，括号内的模式可以嵌套使用，形成复杂的匹配结构和逻辑关系。

总之，括号 () 在正则表达式中用于创建捕获组或非捕获组，用于分组、捕获、设置优先级和应用逻辑等操作。

"""
import re


# 捕获组示例

text = "Hello, my name is John Doe."
pattern = r"Hello, my name is ([A-Za-z\s]+)\."

match = re.search(pattern, text)
if match:
    name = match.group(1)
    print("Name:", name)


# 非捕获组示例


text = "The car is blue."
pattern = r"The car is (?:red|blue|green)\."

match = re.search(pattern, text)
if match:
    color = match.group()
    print("Color:", color)



















