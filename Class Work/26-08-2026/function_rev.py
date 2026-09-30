def rev_num(n,rem=0,rev=0):

    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10

    print(rev)

n1=int(input("Enter NUmber:"))
rev_num(n1)
    