class Fibo:
    def fibo(self,n1=0,n2=1):
        no = int(input("Enter Terms : "))
        for i in range(no):
            print(n1,end=" ")
            n3 = n1 + n2
            n1 = n2
            n2 = n3

class Prime(Fibo):
    def prime(self,prime=0):
        no = int(input("Enter Number : "))

        for i in range(1, no + 1):
            if no % i == 0:
                prime+= 1

        if prime == 2:
            print("Prime Number!!")
        else:
            print("Not a Prime Number!!")


class Reverse(Prime):
    def reverse(self):
        no = int(input("Enter Number : "))
        rev = 0
        for i in range(no):
            if no==0:
                break
            
            rem = no%10
            rev = rev*10+rem    
            no //= 10

        print("Reverse Number :", rev)


obj = Reverse()

while True:

    menu = """
    Press 1 for Fibo Series
    Press 2 for Prime Number
    Press 3 for Rev Number
    Press 4 for Exit
    """

    print(menu)

    choice = int(input("Enter Choice : "))

    if choice == 1:
        obj.fibo()

    elif choice == 2:
        obj.prime()

    elif choice == 3:
        obj.reverse()

    elif choice == 4:
        print("Thank you")
        break

    else:
        print("Invalid Choice")