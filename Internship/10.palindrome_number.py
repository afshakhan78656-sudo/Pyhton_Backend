#using for loop
'''
no=int(input("Enter Number:"))

rev=0
rem=0
n1=no

while(no!=0):
    rem=no%10
    rev=rev*10+rem
    no//=10

if n1==rev:
    print("Palindrome no!!")

else:
    print("not palindrome no!!")

'''

no=int(input("Enter Number:"))

rev=0
n1=no

for i in range(len(str(no))):
    rem=no%10
    rev=rev*10+rem
    no//=10

if n1==rev:
    print("Palindrome no!!")

else:
    print("not palindrome no!!")