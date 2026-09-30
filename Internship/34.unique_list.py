l=[1,2,3,1,2]
uni=[]
dup=[]

for i in l:
    if i not in uni:
        uni.append(i)

    else:
        dup.append(i)

print("Original list:",l)
print("Unique list:",uni)
print("Duplicate list:",dup)