import random

otp=random.randint(1001,9999)

d={}

while True:

    menu="""
        Press 1 for Sign up
        Press 2 for Login
        Press 3 for Forget-Password
        Press 4 for Exit

"""

    print(menu)
    choice=int(input("Entre the Choice:"))

    if choice==1:
        name=input("Enter Name:")
        email=input("Enter Email:")
        mobile=int(input("Enter Mobile:"))
        password=input("Enter Password:")
        cpassword=input("Enter Confirm Password:")

        if password==cpassword:
            d['email']=email
            d['mobile']=mobile
            d['password']=password

            print("Signup Successfully!!")

        else:
            print("Password & Confirm Password does not match!!")


    elif choice==2:
        email=input("Enter Email:")
        password=input("Enter Password:")

        if d['email']==email and d['password']==password:
            print("Login Successfully!!")

        else:
            print("Invalid Credentials!!")

    elif choice==3:
        mobile=int(input("Enter Mobile:"))
        
        if d['mobile']==mobile:
            print("**********Yout opt is:",otp)

            uotp = int(input("Enter OTP:"))

            if otp==uotp:
                password=(input("Enter Password:"))

                d['password']=password
                print("Password updated!!")

            else:
                print("Invalid otp!!")

        else:
            print("Mobile number does not exist!!")

    elif choice==4:
        print("Thank uh!!")
        break