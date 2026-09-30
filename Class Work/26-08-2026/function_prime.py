#Prime
#default Parameter
def prime(n,prime=0):
    for i in range(1,n+1):
        if(n%i==0):
            prime+=1

    if(prime==2):
        print("Prime No!!")

    else:
        print("Not Prime!!")
n=int(input("Enter Numer:"))
prime(n)
       