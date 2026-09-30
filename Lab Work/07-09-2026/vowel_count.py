#Vowels Count

s=input("Enter Name:")
count=0
for i in s:
        if i in 'aeiouAEIOU':
            print("Vowels found:",i)
        count+=1
print()
print("Vowels Count:",count)

#another way using if 
'''
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':

'''