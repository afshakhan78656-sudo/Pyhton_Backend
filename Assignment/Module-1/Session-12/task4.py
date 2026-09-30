#lambda + filter() — Product Names

products = input("Enter products: ").split()
result = list(filter(lambda x: x.startswith("M"), products))

print(result)