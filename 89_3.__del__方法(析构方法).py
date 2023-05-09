"""
__del__
析构方法  (拆解构造)
触发时机：当对象空间不在被任何实例引用（没有任何变量引用）的时候被触发
参数：一个self接收当前对象
返回值：无
作用：使用完对象是回收资源
注意：del不一定会触发当前方法，只有当前对象没有任何变量接收时才会触发
"""


class MyClass:
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f"{self.name} object has been deleted")


# 创建 MyClass 类的实例
obj1 = MyClass("Object 1")

# 创建另一个 MyClass 类的实例，并将其赋值给 obj2 变量
obj2 = MyClass("Object 2")

# 用obj3指向obj1指向的空间
obj3 = obj1

# 删除 obj1 变量引用的对象
del obj1

# 删除 obj2 变量引用的对象
del obj2

# 看obj3是否仍能使用
print(obj3.name)


# Object 2 object has been deleted  del在对象没有用(该空间不再被引用访问时)时才会触发 此时object1指向的空间仍然有用, 因此并没有被删去
# Object 1
# Object 1 object has been deleted

# 注意: python解释器得垃圾回收机制, 在程序执行完成后, 也会回收所有在本次执行过程中使用到的空间,此时也会调用del


