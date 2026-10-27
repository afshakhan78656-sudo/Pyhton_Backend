import random

otp = random.randint(1001, 9999)

d = {}

while True:

    menu = """
        Press 1 for Sign up
        Press 2 for Login
        Press 3 for Forget-Password
        Press 4 for Exit
    """

    print(menu)

    try:
        choice = int(input("Enter the Choice: "))

        if choice == 1:
            name = input("Enter Name: ")
            email = input("Enter Email: ")
            mobile = int(input("Enter Mobile: "))
            password = input("Enter Password: ")
            cpassword = input("Enter Confirm Password: ")

            if password == cpassword:
                d['name'] = name
                d['email'] = email
                d['mobile'] = mobile
                d['password'] = password

                print("Signup Successfully!!")

            else:
                print("Password & Confirm Password does not match!!")


        elif choice == 2:
            email = input("Enter Email: ")
            password = input("Enter Password: ")

            try:
                if d['email'] == email and d['password'] == password:
                    print("Login Successfully!!")
                else:
                    print("Invalid Credentials!!")

            except KeyError:
                print("Please Sign up first!!")


        elif choice == 3:
            mobile = int(input("Enter Mobile: "))

            try:
                if d['mobile'] == mobile:

                    print("********** Your OTP is:", otp)

                    uotp = int(input("Enter OTP: "))

                    if otp == uotp:
                        password = input("Enter New Password: ")

                        d['password'] = password

                        print("Password updated!!")

                    else:
                        print("Invalid OTP!!")

                else:
                    print("Mobile number does not exist!!")

            except KeyError:
                print("Please Sign up first!!")


        elif choice == 4:
            print("Thank You!!")
            break

        else:
            print("Please enter choice between 1 to 4!!")


    except ValueError:
        print("Please enter numbers only!!")

    except Exception as e:
        print("Invalid Input!!", e)
        