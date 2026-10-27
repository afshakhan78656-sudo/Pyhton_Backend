class A:
    def func1(self):
        print("Method 1!!")

class B(A):
    def func2(self):
        print("Method 2!!")

class C:
    def func3(self):
        print("Method 3!!")

class D(B,C):
    def func4(self):
        print("Method 4!!")

obj=D()
obj.func1()
obj.func2()
obj.func3()
obj.func4()