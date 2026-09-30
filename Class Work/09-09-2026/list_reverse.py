#list reverse without built-in function

l=[56, 32, 24, 16, 21]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        l[i],l[j]=l[j],l[i]

print("Reversed List:",l)
