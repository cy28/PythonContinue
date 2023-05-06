class Math:

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y
# 在这个例子中，我们定义了一个名为Math的类，其中包含了两个静态方法add和subtract。
# 这两个方法都不需要访问类或实例的属性或方法，因此它们可以被定义为静态方法。
# 静态方法通常用于封装一些通用的操作，这些操作与类或实例无关。它们可以在类内部使用，也可以在类外部直接使用，而不需要创建类或实例的对象。
# 例如，在上面的Math类中，add和subtract方法是两个通用的数学操作，可以直接调用而不需要创建Math对象。
# 下面是使用Math类的示例：


print(Math.add(2, 3))       # 输出：5
print(Math.subtract(5, 2))  # 输出：3





















