''' def func1():
    a=30
    b=50

    return a+b

print("Addition is:",func1())
'''

''' def fact():
    fact=1
    i=1
    n=5

    while(i<=n):
        fact=fact*i
        i+=1

    return fact

print("Factorail is:",fact())
'''

def rev(n,rev=0,rem=0):
   

    while(n!=0):
        rem=n%10
        rev=rev*10+rem
        n//=10

    return rev

n=int(input("Enter Number:"))

print("Reverse is:",rev(n))


