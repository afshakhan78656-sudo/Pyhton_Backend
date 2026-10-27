class A:
    def func1(self):
        print("Method 1!!")

class B(A):
    def func2(self):
        print("Method 2!!")

class C(A):
    def func3(self):
        print("Method 3!!")

obj=B()
obj1=C()
obj.func1()
obj.func2()
obj1.func3()
