n=int(input("Enter Number:"))

sum=0
i=1

while(i<=n):    #1 2 3 4 5
    sum+=i      #0+1=1  1+2=3   3+3=6   6+4=10 10+5=15
    print(i)    #1  3   6   10  15

    i+=1    #2 3 4 5 (6-false)

print("Sum is:",sum)

