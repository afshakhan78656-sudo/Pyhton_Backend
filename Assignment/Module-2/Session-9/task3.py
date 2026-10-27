#filter() condition ke according items select karta hai.

users = [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]

result = list(filter(lambda x: x[1] > 1000, users))

for i in result:
    print(i[0])

