try:
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity
    print("Total:", total)

except ValueError:
    print("Error: Please enter numeric values!")