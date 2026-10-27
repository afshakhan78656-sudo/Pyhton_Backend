def calculate_total(price, quantity):

    print("Total price is:",end=" ")
    return price * quantity


price = int(input("Enter Price:"))
quantity = int(input("Enter Quantity:"))
print(calculate_total(price, quantity))