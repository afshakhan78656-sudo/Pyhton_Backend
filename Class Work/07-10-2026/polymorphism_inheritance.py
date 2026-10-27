# class Override:
#     def func1(self):
#         print("Method 1!!")

# class Oveerride1(Override):
#     def func1(self):
#         print("Method 2!!")

# obj=Oveerride1()
# obj.func1()



class A:
    def func1(self):
        print("Method 1!!")

class B:
    def func1(self):
        super().func1()
        print("Method 2!!")

class C(B,A):
    def func1(self):
        super().func1()
        print("Method 3!!")

obj=C()
obj.func1()