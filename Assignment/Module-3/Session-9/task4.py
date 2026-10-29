import re

orders = input("Enter order IDs separated by space: ").split()

for order in orders:
    if re.match(r"^ORD\d*[02468]$", order):
        print(order)