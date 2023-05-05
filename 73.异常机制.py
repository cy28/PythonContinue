# 语法错误 就是代码底下出现红色波浪线的情况
# 异常 是程序没有出现红色波浪线的语法错误, 但是程序运行的时候报错
"""
举例:
def chu(a, b):
    return a / b

x = chu(4, 0)  # ZeroDivisionError: division by zero
"""
"""
异常处理的语法
try:
    # 可能会出现异常的代码块
except ExceptionType:
    # 处理特定类型的异常
except:
    # 处理所有其他类型的异常
else:
    # 如果try块中没有出现异常，执行else块中的代码
finally:
    # 无论是否有异常，都会执行finally块中的代码
    
"""


def compute():
    try:
        n1 = int(input('请输入第一个数字: '))
        n2 = int(input('请输入第二个数字: '))
        operation = input('请输入操作符(+ - * /)')

        if operation == '+':
            result = n1 + n2
        elif operation == '-':
            result = n1 - n2
        elif operation == '*':
            result = n1 * n2
        elif operation == '/':
            result = n1 / n2
        else:
            print('无效的操作符!!!')

        print('两个数的运算结果是: ', result)
    except ZeroDivisionError:
        print('除数不能为0!!!')
    except ValueError:
        print('请输入数字进行运算!!!')

compute()

# def compute():
#     n1 = int(input('请输入第一个数字: '))
#     n2 = int(input('请输入第二个数字: '))
#     operation = input('请输入操作符(+ - * /)')
#
#     # 将操作符和两个数字组合成一个字符串表达式
#     expr = str(n1) + operation + str(n2)
#
#     try:
#         # 使用 eval() 函数进行求值
#         result = eval(expr)
#     except ZeroDivisionError:
#         print('除数不能为0')
#         return
#     except:
#         print('无效的输入')
#         return
#
#     print('两个数的运算结果是: ', result)









