"""
1. if单分支语句：
if 表达式：
   执行语句  # 注意执行语句前面要强制缩进四个空格
表达式为True，则执行执行语句，若表达式不成立，则跳过该结构
"""

age = int(input("请输入你的年龄："))
if age >= 18:
    print("欢迎光临！")

print("未成人不得进入！")  # 不管有没有if 这句话都会输出


"""
2. if-else双分支语句：
if 表达式：
    执行语句1
else:
    执行语句2
假如表达式成立就执行语句1，若表达式不成立，则执行语句2.
"""

age1 = int(input("请输入你的年龄："))
if age1 >= 18:
    print("欢迎光临！")
else:
    print("未成人不得进入！")

"""
3. if-elif-else多分支语句：
if 表达式：
    执行语句1
elif:
    执行语句2
else:
    执行语句3
"""

score = int(input("请输入你的成绩："))

if score > 90:
    print("优秀")
elif score > 80:
    print("良+")
elif score > 70:
    print("良")
elif score > 60:
    print("一般")
else:
    print("不及格")


















