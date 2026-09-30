l=[1,2,3,4,5]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        l[i],l[j]=l[j],l[i]

print("Reversed list:",l)