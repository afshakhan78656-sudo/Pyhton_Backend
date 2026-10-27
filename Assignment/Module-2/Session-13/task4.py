ratings = [[4, 5, 3, 2], [5, 4, 4, 3], [3, 2, 5, 5]]

a = []

for x in ratings:
    for i in x:
        if i > 4:
            a.append(i)

print(a)