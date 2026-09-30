l=[56,32,45,12,23,21,16]
print("Original list is:",l)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print("Sorted list is:",l)


