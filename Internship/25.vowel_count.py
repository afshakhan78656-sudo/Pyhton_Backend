s=(input("Enter String:"))
count=0

for i in s:
    if i in 'aeiouAEIUO':
        count+=1

print("Vowels are:",count)
