#four greater without using and operator

n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
n3=int(input("Enter n3:"))
n4=int(input("Enter n4:"))

if n1>n2:
    if n1>n3:
        if n1>n4:
            print("n1 is greater")

        else:
            print("n4 is greater")

    else:
        if n3>n4:
            print("n3 is greater")

        else:
            print("n4 is greater")

else:
    if n2>n3:
        if n2>n4:
            print("n2 is greater")

        else:
            print("n4 is greater")

    else:
        if n3>n4:
            print("n3 is greater")

        else:
            print("n4 is greater")