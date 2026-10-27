names = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

a = []

for i in range(len(names)):
    if prices[i] > 1000:
        a.append((names[i], prices[i]))

print(a)