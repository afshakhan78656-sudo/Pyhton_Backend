# t=(1,2,"a","b",5.6,10,1,1,True)

# print(type(t))

# print(t)

# print(t.count(1))

# print(t.index("a"))


#tup to list

t=(1,2,"a","b",5.6,True,10,1,1,3)
print(t)

l=list(t)
print("Tuple to List:",l)

l.append(100)

t=tuple(l)
print("After Append Tuple is:",t)