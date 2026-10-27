#Single inheritance
# class A:
#     def func1(self):
#         print("Method 1!!")

# class B(A):
#     def func2(self):
#         print("Method 2!!")

# obj=B()
# obj.func1()
# obj.func2()

#Multi-level Inheritance

class A:
    def func1(self):
        print("Method 1!!")

class B(A):
    def func2(self):
        print("Method 2!!")

class C(B):
    def func3(self):
        print("Method 3!!")

obj=C()
obj.func1()
obj.func2()
obj.func3()