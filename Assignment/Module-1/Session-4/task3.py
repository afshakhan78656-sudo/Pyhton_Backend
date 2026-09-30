age=int(input("Enter the Age:"))
time=int(input("Enter the Time:"))

if age>=18:
    if time>=22 or time<=2:
        print("Order allowed!!")

    else:
        print(" Order Not allowed")

else:
    print("You are not eligible , Order not allowed!!")