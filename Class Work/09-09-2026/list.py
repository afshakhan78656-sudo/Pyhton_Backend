# #even odd list
# no=int(input("Enter Number:"))
# l=[]
# ev=[]
# od=[]

# for i in range(1,no+1):
#     l.append(i)

#     if i%2==0:
#         ev.append(i)

#     else:
#         od.append(i)

# print(l)
# print("Even List:",ev)
# print("Odd List:",od)



#unique list
# l=[1,2,3,1,2]
# uni=[]
# dup=[]

# for i in l:
#     if i not in uni:
#         uni.append(i)
    
#     else:
#         dup.append(i)

# print("Original List:", l)
# print("Unique List:", uni)
# print("Duplicate List:", dup)



#sorting
l=[56,32,24,16,21]
l.sort()
print("Sorted List:", l)
print("Smallest:",l[0])
print("Second Smallest:",l[1])
print("Largest:",l[-1])
print("Second Largest:",l[-2])


# task :1 

"""
seprate  the  pelindrome string and store to  another list.  hint  : try to solve  using slicing.
l1= ["maam","php" ,"java" ,"c++"]
output  : l1 =["maam","php"]
"""

l1= ["maam","php" ,"java" ,"c++"]
print("palindrome strings:")
print(l1[0:2])

#another var
l1= ["maam","php" ,"java" ,"c++"]
l2=[]
for i in l1:
    if i==i[::-1]:
        l2.append(i)

print(l2)