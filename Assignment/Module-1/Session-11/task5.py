def update_cart(cart, item, qty):
    cart.update({item: qty})
    return cart


cart = {
    "Mobile": 1,
    "Shoes": 2
}

print(update_cart(cart, "Laptop", 1))
print(update_cart(cart, "Shoes", 3))