
# t=(1,2,"HELLO","WORLD",3.14,True,1,1)
# print(type(t))

# print("Tuple:",t)

# print(t.count(1))

# print(t.index("HELLO"))


t=(1,2,"HELLO","WORLD",3.14,True,4,5)
l=list(t)
print("List:",l)

l.append(100)

t=tuple(l)
print("Revised Tuple:",t)
