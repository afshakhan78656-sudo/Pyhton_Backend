#prime or not --- jo khud ke table me aata ho jajise 7,11,13    (2 times chcek karta hai)

n=int(input("Enter Number:"))

prime=0
for i in range(1,n+1):
    if(n%i==0):  
        prime+=1

if(prime==2):
    print("Prime Number!!")

else:
    print("Not Prime Number!!")
