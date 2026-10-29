class Payment:
    def pay(self, amount):
        print("Paying", amount)

class UPI(Payment):
    def pay(self, amount):
        super().pay(amount)
        print("Paying", amount, "via UPI")

obj = UPI()
obj.pay(500)
