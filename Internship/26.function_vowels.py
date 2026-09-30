def vowels(s,count=0):
    for i in s:
        if i in 'aeiouAEIUO':
            count+=1

    print("Vowels are:",end=" ")
    return count

s=input("Enter String:")
print(vowels(s))