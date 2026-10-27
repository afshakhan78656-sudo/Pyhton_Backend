class A:
    def func1(self):
        print("Method 1!!")

class B:
    def func2(self):
        print("Method 2!!")

class C(A,B):
    def func3(self):
        print("Method 3!!")

obj=C()
obj.func1()
obj.func2()
obj.func3()