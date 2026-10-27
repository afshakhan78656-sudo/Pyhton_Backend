class Bank:

    def ac_register(self):
        name=input("Enter Name:")
        mobile=int(input("Enter Mobile:"))
        password=int(input("Enter Password:"))
        bal=5000
        ac_no=12345
        print("Your account is open and initial balance is:")
        print("Account number is:",ac_no)
        self.bal=bal

    def deposite(self):
        damount=int(input("Enter Deposite Amount:"))
        self.bal+=damount
        print("Deposite Successfully!!")

    def withdraw(self):
        wamount=int(input("Enter Deposite Amount:"))
        self.bal-=wamount
        print("Withdraw Successfully!!")

    def chec_bal(self):
        print("Balance:",self.bal)


obj=Bank()

menu="""
    press 1 for Account Register
    press 2 for Exit
"""
print(menu)
choice=int(input("Enter your choice:"))

if choice==1:
    obj.ac_register()
while True:

    menu1="""
        press 1 for Deposit
        press 2 for Withdraw
        press 3 for Check Balance
        press 4 for Exit
    """
    print(menu1)
    choice1=int(input("Enter your choice:"))

    if choice1==1:                  
        obj.deposite()

    elif choice1==2:
        obj.withdraw()

    elif choice1==3:
        obj.chec_bal()
        
    elif choice1==4:
        print("Thank uh!!")
        break
    else:   
        print("Invalid Choice!!")
        break

     

