# try:
#     n=int(input("Enter a number: "))

#     if n==0:
#         print("Zero!!")

#     else:
#         print("Not Zero!!")

# except ValueError as e:
#     print(e)

# else:
#     print("Try Here!!")

# finally:
#     print("Everytime!!")



#1) value error
#2) ZeroDivisionError

# try:
#     n1=int(input("Enter Number1: "))
#     n2=int(input("Enter Number2: "))

#     print("Division is: ",n1/n2)

# except ValueError as e:
#     print(e)

# except ZeroDivisionError as e:
#     print(e)




#1) ValueError and IndexError 
# try:
#     l=[67,72,45,12,90]

#     n=int(input("Enter Index: "))
#     print("Value od Index:",l[n])

# except ValueError as e:
#     print(e)

# except IndexError as e:
#     print(e)




try:
    l=[67,72,45,12,90]

    n=int(input("Enter Index: "))
    print("Value of Index:",l[n])

except Exception as e:
    print(e)
    print("Invalid Input!!")

