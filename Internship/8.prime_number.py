#using while loop
'''
no=int(input("Enter Number:"))

i=1
prime=0
while i<=no:
    if no%i==0:
        prime+=1

    i+=1

if prime==2:
    print("Prime!!")

else:
    print(" not prime!!")
'''

#using for loop

no=int(input("Enter Number:"))

i=1
prime=0

for i in range(1,no+1):
    if no%i==0:
        prime+=1

    i+=1

if prime==2:
    print("prime!!")

else:
    print("not prime!!")