no=int(input("Enter Number:"))

l=[]
ev=[]
od=[]

for i in range(1,no+1):
    l.append(i)

    if i%2==0:
        ev.append(i)

    else:
        od.append(i)

print("Original list is:",l)
print("Even list is:",ev)
print("Odd List is:",od)



