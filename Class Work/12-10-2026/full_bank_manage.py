import random
class Bank:
    def ac_register(self):
        ac_no=random.randint(1000,9999)
        name=input("Enter the name of the account:")
        password= int(input("Enter the password :"))
        mobile= int(input("Enter the mobile number :"))
        bal=50000
        print("Your account is open and initial balance is ",bal)
        print("Your account number is ",ac_no)
        self.bal=bal
        
    def deposit(self):
        damount=int(input("Enter the amount to deposit :"))
        if damount>=10000:
            print("Insufficient Balance")
            return  
        self.bal+=damount
        print("Your current balance is ",self.bal)

    def withdraw(self):
        wamount=int(input("Enter the amount to withdraw :"))
        if wamount>=10000:
            print("Please enter a valid amount")
            return
        self.bal-=wamount
        print("Your current balance is ",self.bal)
        
    def check_bal(self):
        print("Your current balance is ",self.bal)
        
obj=Bank()

menu="""
    Press 1 for Account Opening
    press 2 for Exit
"""
print(menu)
    
choice=int(input("Enter your choice :"))
if choice==1:
    obj.ac_register()
    
while True:
    
    menu1="""
    Press 1 for Deposit
    Press 2 for Withdraw
    Press 3 for Check Balance
    Press 4 for Exit
    """
    print(menu1)
    choice1=int(input("Enter your choice :"))
    
    if choice1==1:
        obj.deposit()

    elif choice1==2:
        obj.withdraw()

    elif choice1==3:
        obj.check_bal()

    elif choice1==4:
        break

    else:
        break
        print("Invalid Choice!!")