#using thired variable.

'''
a=int(input("Enter a:"))
b=int(input("Enter b:"))

print("Before Swapping:",a,b)
temp=a
a=b
b=temp

print("After Swapping:",a,b)


#withot using 3rd variable
a=int(input("Enter a:"))
b=int(input("Enter b:"))

print("Before Swapping:",a,b)
a=a+b
b=a-b
a=a-b

print("After Swapping:",a,b)

'''

#in py
a=int(input("Enter a:"))
b=int(input("Enter b:"))

print("Before Swapping:",a,b)
a,b=b,a

print("After Swapping:",a,b)
