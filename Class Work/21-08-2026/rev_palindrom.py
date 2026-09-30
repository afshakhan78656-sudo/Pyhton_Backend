# reverse and palindrome

n=int(input("Enter Number:"))

rem=0
rev=0
n1=n

while(n!=0):
    rem=n%10    #5836%10= 583.6   58.3
    rev=rev*10+rem  #0+6=6  60+3=63
    n//=10      #583    58

print(rev)

'''if(n1==rev):
    print("Palindrom!!")

else:
    print("Not Palindrome!!")
    '''


#using for loop
'''
n = int(input("Enter number: "))

reverse = 0


for i in range(5):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print("Reverse:", reverse)
'''