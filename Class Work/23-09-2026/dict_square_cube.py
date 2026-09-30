# #sqauare dict
# d={}

# for i in range(1,31):
#     d[i]=i*i

# print(d)


#name me letter count

# s=input("Enter Name:").lower()
# # d={}

# # for i in s:
# #     if i in d:
# #         d[i]+=1

# #     else:
# #         d[i]=1

# # print(d)


#task

d={'p':400,'q':100,'r':250}
d1={'p':200,'q':100}

for i in d1:
    if i in d:  
        d[i]+=d1[i]

    else:
        d[i]=d1[i]
print(d) 


#sum of dict by sir

""" d = {'p':400,'q':100,'r':250}
d1 = {'p':200,'q':100}

ans = {}

for i,j in d.items():
    for k,l in d1.items():
        if i == k:
            ans[i] = j + l

        if i not in ans:
            ans[i] = j

print(ans) """