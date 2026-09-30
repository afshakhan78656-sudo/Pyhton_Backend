#1.default function

""" def rev_number():
    no=int(input("Enter Number:"))
    rem=0
    rev=0

    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10

    print(rev)

rev_number()

 """

#2.function with parameters and without args
""" def rev_number(no,rem=0,rev=0):   #create krte time parameters dete hai ex.no
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10

    print(rev)

no=int(input("Enter Number:"))
rev_number(no)  #call krte time argumrents dete hai  ex.no
 """

#3.function without parametres and return types.

""" def rev_number():
    no=int(input("Enter Number:"))

    rev=0
    rem=0
    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10

    return rev

print(rev_number()) """

#4.function with parameters and with return type

def rev_number(no,rem=0,rev=0): #with para 

    while(no!=0):
        rem=no%10
        rev=rev*10+rem
        no//=10

    return rev  #with return type

no=int(input("Enter Number:"))
print(rev_number(no))