#sorting without using built-in function
l = [56, 32, 24, 16, 21]

for i in range(len(l)):
    for j in range(i+1, len(l)): 
        if l[j] < l[i]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp

print("Sorted List:", l)