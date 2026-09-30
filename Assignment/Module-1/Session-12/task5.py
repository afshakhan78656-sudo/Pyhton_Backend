#reduce() + lambda — Total Bill

from functools import reduce

prices = input("Enter prices: ").split()
prices = list(map(int, prices))
total = reduce(lambda x, y: x + y, prices)

print("Total Bill:", total)