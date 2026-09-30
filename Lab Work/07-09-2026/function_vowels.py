def vowels(s):
    count=0
    for i in s:
        if i in 'aeiouAEIOU':
            count+=1

    return count

s=input("Enter String:")
print("vowels Count:", vowels(s))
