import sys
sys.path.append('.\98_1_1.自定义模块')


# 导入自定义模块
import my_module2

# 使用属性
print(my_module2.my_variable)

# 使用函数
result = my_module2.square(5)
print(result)

# 使用类
my_dog = my_module2.Dog("Fido", 3)
my_dog.bark()
