#Swapping :2 ways se

#1: with using third variable
#a=100 b=50

#temp=a    #temp=100 a=blank
#a=b       #a=50 b=blank
#b=temp     #b=100 temp=blank

#2:Without using third Variable.
#a=a+b  #100+50  a=150
#b=a-b  #150-50  b=100
#a=a-b  #150-100  a=50

#in py 

a=int(input("Enter A:"))
b=int(input("Enter B:"))
a,b=b,a

print("After Swapping:")

print("A is:",a)
print("B is:",b)