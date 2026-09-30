#factorial :5*4*3*2*1

n=int(input("Enter Number:"))

fact=1
i=1

while(i<=n):
    fact=fact*i     #1*1=1  1*2=2  2*3=6 6*4=24  24*5=120
    i=i+1

print(fact)
