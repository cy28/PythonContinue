import pymysql
import pymysql

# 建立数据库连接
conn = pymysql.connect(
    host='127.0.0.1',
    user='root',
    port=3306,
    password='19991030',
    charset='utf8'
)

# 创建游标对象
cursor = conn.cursor()
# cursor = conn.cursor()这行代码的作用是创建一个光标对象，以便你可以通过这个对象来执行SQL查询和检索结果，以及管理你的数据库交易。

# ---------------------------------------------------------------------------------------------

# 1. 查看数据库

# 发送指令
cursor.execute("show databases")

# 获取指令的结果
result = cursor.fetchall()

# 打印获取的结果
print(result)

# ------------------------------------------------------------------------------------------------

# # 2. 创建数据库 字符集和校对规则
#
# # 发送指令
# cursor.execute(create database ***database_name*** default charset uft8 collate uft_general_ci)
#
# # 提交事务
# conn.commit()
#
# # 3. 删除数据库
# cursor.execute("drop database ***database_name***")
#
# # 提交事务
# conn.commit()


# 关闭游标和连接
cursor.close()
conn.close()


























