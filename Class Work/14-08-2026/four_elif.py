n1 = int(input("Enter n1: "))
n2 = int(input("Enter n2: "))
n3 = int(input("Enter n3: "))
n4 = int(input("Enter n4: "))

if n1 > n2:
    if n1 > n3:
        if n1 > n4:
            print("Greatest:", n1)
        else:
            print("Greatest:", n4)
    else:
        if n3 > n4:
            print("Greatest:", n3)
        else:
            print("Greatest:", n4)
else:
    if n2 > n3:
        if n2 > n4:
            print("Greatest:", n2)
        else:
            print("Greatest:", n4)
    else:
        if n3 > n4:
            print("Greatest:", n3)
        else:
            print("Greatest:", n4)