class A:

    def func1(self):

        a=10
        self.a=a

    def func2(self):
        print(self.a)


obj=A()
obj.func1()
obj.func2()