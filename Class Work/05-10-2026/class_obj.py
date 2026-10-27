class MyClass:
    def even_odd(self,no):
        if no%2==0:
            print("even no!!")

        else:
            print("odd no!!")

    def prime(self,no,prime=0):
        for i in range(1,no+1):
            if no%i==0:
                prime+=1

        if prime==2:
            print("Prime no!!")

        else:
            print("Not prime no!!")

    def fact(self,no,fact=1):
        for i in range(1,no+1):
            fact=fact*i

        print("Factorial is:",fact)

    def reverse(self,no,rev=0,rem=0):
        for i in range(no):
            if no==0:
                break

            rem=no%10
            rev=rev*10+rem
            no//=10

        print("Reverse no is:",rev)



no=int(input("Enter No:"))
obj=MyClass()
obj.even_odd(no)
obj.prime(no)
obj.fact(no)
obj.reverse(no)