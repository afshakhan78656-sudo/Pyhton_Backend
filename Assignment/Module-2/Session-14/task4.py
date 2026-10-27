orders = {}

def add_order(order_id, restaurant, total):
    orders[order_id] = {"restaurant": restaurant, "total": total}

def update_total(order_id, total):
    if order_id in orders:
        orders[order_id]["total"] = total

add_order(101, "Dominos", 500)
update_total(101, 700)

print(orders)