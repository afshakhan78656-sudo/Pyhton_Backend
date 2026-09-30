def fibonaaci(no,n1=0,n2=1):
    for i in range(no):
        print(n1,end=" ")

        n3=n1+n2
        n1=n2
        n2=n3

    return n1

no=int(input("Enter Number:"))
fibonaaci(no)