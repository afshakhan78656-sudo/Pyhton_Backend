def palindrome_number(no,rev=0,rem=0):
    n1=no
    for i in range(no):
        if no==0:
            break

        rem=no%10
        rev=rev*10+rem
        no//=10

    if n1==rev:
        print("Pliandrome!!")

    else:
        print("not palindrome!!")
    
    return rev

no=int(input("Enter Number:"))
palindrome_number(no)
