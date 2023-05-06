# 情况1 大范围的异常类型要放在except的后面
# def compute():
#     try:
#         n1 = int(input('请输入第一个数字: '))
#         n2 = int(input('请输入第二个数字: '))
#         operation = input('请输入操作符(+ - * /)')
#
#         if operation == '+':
#             result = n1 + n2
#         elif operation == '-':
#             result = n1 - n2
#         elif operation == '*':
#             result = n1 * n2
#         elif operation == '/':
#             result = n1 / n2
#         else:
#             print('无效的操作符!!!')
#         print('两个数的运算结果是: ', result)
#         # 文件操作可能出现文件找不到的情况
#         with open('0.test_document/test4_74', 'w') as w_stream:
#             w_stream.write(str(result))
#         with open('0.test_document/test4_74_error', 'r') as r_stream:  # 读一个不存在的文件
#             print(r_stream.read())
#
#     except ZeroDivisionError:
#         print('除数不能为0!!!')
#     except ValueError:
#         print('请输入数字进行运算!!!')
#     except Exception:
#         print('出错了!!!')
#
# compute()
#

# 捕获过程
# 1. 一旦程序无法运行, 就发生了异常. 会产生相应的异常类型
# 2. 接着会拿着产生的异常类型与后面的except部分进行比较
# 3. 匹配的顺序是从上到下的, 所以包含最多异常类型的Exception类型, 得放在最后
# 4. 如果exception放在最开始的地方, 那么一开始就会报错(出错了)

# 情况2 可以用except Exception as err得形式, 返回异常的类型
# except ZeroDivisionError:
# print('除数不能为0!!!')
# except ValueError:
# print('请输入数字进行运算!!!')
# except Exception as err:  # 如果无法判断后面的异常类型, 可以通过这种形式, 不仅报出异常, 还给出异常的类型
# print('出错了!!!', err)


# 情况3  如果用了else, try代码块中, 不能用return

# def func():
#     try:
#         n = int(input('输入数字: '))
#         print(n)
#         return 1
#     except:
#         print('必需输入数字')
#         return 2
#     else:
#         print('数字输入完毕')  # 没有异常才会执行的代码块

# 情况4

"""
try:
# 可能会出现异常的代码块

except:  
# 处理所有其他类型的异常


finally:  
# 无论是否有异常，都会执行finally块中的代码, 且前面如果有return, 这里finally还是要执行
# 且如果finally有return, 会把之前的return覆盖掉
"""


def func1():
    stream = None
    try:
        stream = open("0.test_document/test4_74", 'r')
        content = stream.read()
        print(content)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('----------------finally---------------------')
        if stream:
            stream.close()
        return 3


print(func1())  # 3











