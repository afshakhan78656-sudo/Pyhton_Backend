def prime(no, i=2):

    if no == i:
        return False

    if no % i == 0:
        return True

    return prime(no, i + 1)

no = int(input("Enter No: "))

if prime(no):
    print("Prime")
else:
    print("Not Prime")