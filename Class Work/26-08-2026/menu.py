while True:
    menu="""

    press 1 for Fibo Series
    press 2 for Prime Number
    press 3 for Rev Number
    press 4 for Exit

"""

    print(menu)
    choice=int(input("Enter Choice:"))

    #Fibonacci 0 1 pehle se to 0 1 ka ans 1 then 1 1 ka 2 then 1 2 ka 3 aese n numbers tak
    if choice==1:
        n=int(input("Enter Terms:"))
        n1=0
        n2=1

        print(n1)
        print(n2)

        for i in range(3,n+1):
            n3=n1+n2
            print(n3)
            n1=n2
            n2=n3

    #Prime or not
    elif choice==2:
        n=int(input("Enter Numbers:"))
        prime=0

        for i in range(1,n+1):
            if(n%i==0):
                prime+=1

        if(prime==2):
            print("Prime no!!")

        else:
            print("Not Prime!!")


    #Reverse Number
    elif choice==3:
        n=int(input("Enter Number:"))
        rem=0
        rev=0
        n1=n

        while(n!=0):   
            rem=n%10
            rev=rev*10+rem
            n//=10

        print(rev)


    elif choice==4:
        print("Thank You!!")
        break

    else:
        print("Invalid Choice!!")
        break