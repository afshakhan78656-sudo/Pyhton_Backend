class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    def show_order(self):
        print("Restaurant:", self.restaurant_name)
        print("Items:", self.items)
        print("Total Price:", self.total_price)


o1 = FoodOrder("Dominos", ["Pizza", "Coke"], 500)

o1.show_order()