def fact(no,fact=1):
    for i in range(1,no+1):
        fact=fact*i

    return fact

no=int(input("Enter Number:"))
print(fact(no))
