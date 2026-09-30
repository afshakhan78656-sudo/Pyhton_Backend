#using for loop

no=int(input("Enter the Terms:"))

n1=0
n2=1

for i in range(no):
    print(n1,end=" ")

    n3=n1+n2
    n1=n2
    n2=n3


#using while 

no=int(input("Enter No:"))

n1=0
n2=1
i=1

while i<=no:
    print(n1,end=" ")
    i+=1
    n3=n1+n2
    n1=n2
    n2=n3
