#using while loop

'''
no=int(input("Enter Number:"))

fact=1
i=1

while(i<=no):
    fact=fact*i
    i=i+1

print("factorial is:",fact)
'''

#using for loop
no=int(input("Enter Number:"))

fact=1
i=1

for i in range(1,no+1):
    fact=fact*i
    i+=1

print("Fctorial is:",fact)

