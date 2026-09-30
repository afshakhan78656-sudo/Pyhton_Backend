def sum_of_number(no,sum=0):
    for i in range(1,no+1):
        sum+=i
        print(i)

    print("Sum is:")

    return sum

no=int(input("Enter Number:"))
print(sum_of_number(no))