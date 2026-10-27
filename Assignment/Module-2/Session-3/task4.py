restaurants = ["Burger Hub", "Pizza Point", "Sushi House"]
times = [30, 25, 40]

for r, t in zip(restaurants, times):
    print(r, "-", t, "min")