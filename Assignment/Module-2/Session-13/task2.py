songs = [[210, 180, 240], [150, 200], [300, 120, 90]]
a = []

for x in songs:
    for i in x:
        if i > 200:
            a.append(i)

print(a)