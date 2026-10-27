teams=["RCB","GT","CSK","MI"]
points=[12,8,15,17]

d=dict(zip(teams,points))

for i in d:
    if d[i]>10:
        print(i,":",d[i])
