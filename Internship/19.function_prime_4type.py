def prime(no,prime=0):
    for i in range(1,no+1):
        if no%i==0:
            prime+=1

    if prime==2:
        print("prime!!")

    else:
        print("not prime!!")

    return prime

no=int(input("Enter Number:"))
prime(no)