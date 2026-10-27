class MyClass:
    def func1(self,__a):
        print("Private method:",__a)
        print("Method 1!!")

    def func2(self):
        print("Method 2!!")

    def func3(self):
        print("Method 3!!")

obj=MyClass()
obj.func1(10)
obj.func2()
obj.func3()