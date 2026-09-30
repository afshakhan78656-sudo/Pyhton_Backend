def fibo(n):

    if n==0:
        return 0

    if n==1:
        return 1

    else:
        return fibo(n-1)+fibo(n-2)
        #0+1=1
        #1+1=2
        #1+2=3
        #2+3=5
        #3+5=8
        #5+8=13
        #8+13=21
        #13+21=34


no=int(input("Enter No:"))
for i in range(no): #11 
    print(fibo(i))
