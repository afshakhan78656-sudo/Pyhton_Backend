#using while loop
'''
no=int(input("Enter Number:"))

rem=0
rev=0

while(no!=0):
    rem=no%10
    rev=rev*10+rem
    no//=10

print("Reverse Numbers are:",rev)
'''

#using for loop

no=int(input("Enter Number:"))

rev=0

for i in range(len(str(no))):
    rem=no%10
    rev=rev*10+rem
    no//=10

print("Reverse Numbers are:",rev)
