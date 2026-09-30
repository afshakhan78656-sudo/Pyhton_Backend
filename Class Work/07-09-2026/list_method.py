l=[10,20,10.7,True,"Hello",1,1]

print(type(l))

l.append(100)  #last me add hoga
print(l)

print(l.count(1))  #count of 1

l.extend([200,300,400])  #last me add hoga multiple data
print(l)

l.insert(2,500)  #2nd index me add hoga
print(l)

l.pop()  #last index ka data remove hoga
print(l)

l.pop(2)  #2nd index ka data remove hoga
print(l)    

l.remove(10)  #10 ka data remove hoga   
print(l)

print(l.index(20))  #20 ka index return hoga  

# print(l.sort()) #sort of list

print(l.clear()) #clear list 


# l=[1,2,3,10.6,3,1,2,]
# l.sort()
# print(l)