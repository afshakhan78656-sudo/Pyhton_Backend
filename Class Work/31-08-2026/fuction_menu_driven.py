while True:
    menu="""
        1.press 1 for (default function) factorial
        2.press 2 for (with para without return type) prime no
        3. press 3 for (without para with raturn type) even_odd
        4.press 4 for (with para with return type) revese no
        5.press 5 for exit
""" 

    print(menu)
    choice=int(input("Enter Terms:"))

    if choice==1:
        #default function.
        def fact(n=5):
            fact=1
            i=1
            for i in range(1,n+1):
                fact=fact*i
                i+=1
            return fact

        print(fact())

    elif choice==2:
            #with para no return type
    
            def prime(n,prime=0):
                for i in range(1,n+1):
                    if(n%i==0):
                        prime+=1
    
                if(prime==2):
                    print("prime!!")
    
                else:
                    print("not prime!!")
    
            n=int(input("Enter Number:"))
            prime(n)

    elif choice==3:
        #without parameter with return type.
        def even_odd(n):
            if(n%2==0):
                print("even!!")

            else:
                print("odd!!")

            return even_odd

        n=int(input("Enter Number:"))
        print(even_odd(n))

    elif choice==4:
        #with parameter with return type.
        def rev(n,rev=0,rem=0):

            while(n!=0):
                rem=n%10
                rev=rev*10+rem
                n//=10

            return rev

        n=int(input("Enter Number:"))
        print("reverse is:",rev(n))

    elif choice==5:
        print("Exit!!")
        break

    else:
        print("Invalid choice!!")