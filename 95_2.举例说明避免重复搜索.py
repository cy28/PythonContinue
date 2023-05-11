# 举例说明 3. 避免重复搜索，即如果两个类都是某个类的直接或间接父类，则只搜索第一个父类。

class A:
    def foo(self):
        print("A's foo method")

class B(A):
    def foo(self):
        print("B's foo method")

class C(A):
    def foo(self):
        print("C's foo method")

class D(B, C):
    pass

# 现在，如果我们创建一个D类的实例d，并调用其foo()方法，那么Python会按照MRO列表的顺序搜索foo()方法。
# 在这个例子中，D的MRO列表为[D, B, C, A, object]。
# 根据广度优先的原则，Python会先搜索B的foo()方法，因为B是D的第一个父类。
# 类D继承自类B和C，而B和C都继承自A，因此在搜索D类的foo()方法时，会首先搜索B类的foo()方法，然后再搜索C类的foo()方法，最后才会搜索A类的foo()方法。
# 当B类中存在foo()方法时，搜索顺序是首先搜索B类，然后是C类，最后是A类。因此，在这个例子中，C类的foo()方法不会被搜索到。





