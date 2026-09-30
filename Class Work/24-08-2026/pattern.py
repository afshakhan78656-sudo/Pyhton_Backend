#Right

""" for i in range(1,6):

    for j in range(1,i+1):
        print("*",end=" ")

    print()


# right in one line
for i in range(1,6):
    print("* "*i)  """

#left

for i in range(1,6):

    for k in range(1,6-i):
        print(" ",end=" ")

    for j in range(1,i+1):
        print("*",end=" ")

    print() 

#left one line

for i in range(1,6):
    print(" "*(6-i),"*"*i) 


#triangle

'''for i in range(1,6):
   
    for k in range(1,6-i):
        print(" ",end="")

    for j in range(1,i+1):
        print(" *",end="")

    print()
'''

#traingle in one line
""" 
for i in range(1,6):
    print(" "*(6-i)," *"*i) """