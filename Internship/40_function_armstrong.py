def armstrong_number(no,sum=0):
    temp=no

    while no>0:
        digit=no%10
        sum=sum+digit**3
        no//=10

    if sum==temp:
        print("armstrong!!")

    else:
        print("not armstrong!!")

    return no

no=int(input("Enter Number:"))
armstrong_number(no)
