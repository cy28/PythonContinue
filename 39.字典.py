"""
在使用列表存储多个数据的时候，在获取和修改数据时，会存在一些缺陷。这个时候引出字典来解决这个问题
字典的语法：
dict1 = {key:value, key:value, key:value}
注意: 在字典中key值是唯一的
"""
# 声明空字典
dict0 = {}
print(type(dict0))  # <class 'dict'>

dict1 = {"name": "张三", "age": "32", "height": 175, "sex": "男", "school": "清华大学", "job": "算法工程师"}
print(dict1)

# 1. 查找字典中元素
# dict[key] 根据索引访问字典中的value值  []中填入要访问的索引值
# 如果访问的时候没有对应的key值，则会报error错
print(dict1['name'])  # 张三

# 也可以通过get(key) 来访问， 参数同样是key值, 如果访问的时候没有对应的key值，则返回的值为None
# 根据key, 得到value值
# get方法可以设置一个默认值, 找不到可以返回一个默认值  get(key, 默认值)

print(dict1.get('job'))  # 算法工程师
print(dict1.get('money'))  # None
print(dict1.get('money', '没有该键值'))  # 没有该键值

# 2. 修改字典中的元素, 原字典存在该键
dict1['name'] = '王五'
print(dict1)  # {'name': '王五', 'age': '32', 'height': 175, 'sex': '男', 'school': '清华大学', 'job': '算法工程师'}

# 3. 字典中添加元素, 原字典中不存在该键
dict1['money'] = '55555'
print(dict1)
# {'name': '王五', 'age': '32', 'height': 175, 'sex': '男', 'school': '清华大学', 'job': '算法工程师', 'money': '55555'}

# 4. 字典中删除元素
# 第一种 pop('要删除元素的key‘)  根据键弹出, 因为键是唯一的, 且删除的是键值对, 返回的是key对应的value值
return1 = dict1.pop('school')
print(dict1)  # {'name': '王五', 'age': '32', 'height': 175, 'sex': '男', 'job': '算法工程师', 'money': '55555'}
print(return1)  # 清华大学

# 第二种 popitem  默认从后往前弹出一个键值, 返回值的形式是元组, (key, value)
return2 = dict1.popitem()
print(dict1)  # {'name': '王五', 'age': '32', 'height': 175, 'sex': '男', 'job': '算法工程师'}
print(return2)  # ('money', '55555')

# 第三种 系统方法 del
del dict1['age']
print(dict1)  # {'name': '王五', 'height': 175, 'sex': '男', 'job': '算法工程师'}

# 第四种 clear() 表示清空字典
dict1.clear()
print(dict1)  # {}


# 5. 获取字典的参数
dict2 = {'name': '中国医生', 'director': '刘伟强', 'actor': '张涵予', 'address': 'Shanghai'}

# 获取字典的长度
print(len(dict2))  # 4

# 获取字典中所有的key值
print(dict2.keys())  # dict_keys(['name', 'director', 'actor', 'address'])

# 获取字典中所有的value值
print(dict2.values())  # dict_values(['中国医生', '刘伟强', '张涵予', 'Shanghai'])

# 获取字典中所有的键值
print(dict2.items())  # dict_items([('name', '中国医生'), ('director', '刘伟强'), ('actor', '张涵予'), ('address', 'Shanghai')])

# 6. 遍历字典

# 方法一：for in

# 如果用for in 直接遍历字典, 则返回的只是key
for i in dict2:
    print(i)
# name
# director
# actor
# address

print(dict2.keys())  # dict_keys(['name', 'director', 'actor', 'address'])
for key in dict2.keys():
    print(key)
# name
# director
# actor
# address

print(dict2.values())  # dict_values(['中国医生', '刘伟强', '张涵予', 'Shanghai'])
for value in dict2.values():
    print(value)
# 中国医生
# 刘伟强
# 张涵予
# Shanghai

print(dict2.items())  # dict_items([('name', '中国医生'), ('director', '刘伟强'), ('actor', '张涵予'), ('address', 'Shanghai')])
for k, v in dict2.items():
    print(k, v)
# name 中国医生
# director 刘伟强
# actor 张涵予
# address Shanghai

# 7. 合并字典 update(合并字典名) 里面的参数填要合并的字典
dict3 = {'name': '成龙', 'sex': '男', 'age': '61'}
dict4 = {'region': '香港'}
dict3.update(dict4)
print(dict3)  # {'name': '成龙', 'sex': '男', 'age': '61', 'region': '香港'}
# 注意: 两个字典之间没有加号合并的形式














