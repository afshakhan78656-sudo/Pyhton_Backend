f = open("orders.txt", "w")

f.write("Pizza\n")
f.write("Burger\n")
f.write("Sandwich\n")
f.write("Pasta\n")
f.write("Cold Coffee\n")

f.close()

f = open("orders.txt", "r")

for order in f:
    print("Order:", order.strip())
    print("Position:", f.tell())

f.close()