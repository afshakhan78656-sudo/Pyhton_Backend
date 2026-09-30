d={1:"Hello",2:"World",3:"Python",4:"Programming"}
print("Dictionary:",d)

print(d.copy()) #copy of dictinoary
print(d.get(2)) #get value of 2
print(d.items()) #get all of dictionary

print(d.keys()) #get keys of dict

print(d.values())  #get values od dict

d.update({5:"is best"}) #update dict
print(d)

d.pop(2) #pop selected key
print(d)

d.popitem() #popss last item
print(d)

t=(1,2,3)
d1={}

print(d1.fromkeys(t,"Hello"))
