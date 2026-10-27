#map() har item par operation karta hai.
prices = [120, 250, 99, 180, 310]

result = list(map(lambda x: x + (x * 0.10), prices))

print(result)