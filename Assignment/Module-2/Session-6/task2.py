username=["Ramesh","Suresh","Hitesh"]
followers=[500,200,1000]

d={}

for i in range(len(username)):
    d[username[i]]=followers[i]

print(d)