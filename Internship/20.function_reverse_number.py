def rev_number(no,rem=0,rev=0):
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10

    return rev

no=int(input("Enter Number:"))
print(rev_number(no))
