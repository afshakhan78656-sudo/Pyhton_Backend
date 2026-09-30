# palindrom with parameter and return type

def palidrome(s):
    if s==s[::-1]:
        return True

    else:
        return False

s=input("Enter Name:")
if palidrome(s):
    print("String is Palindrome!!") 

else:
    print("String is not Palindrome!!")

