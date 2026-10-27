def apply_coupon(amount, coupon_code=None):
    if coupon_code == "SAVE10":
        amount = amount * 0.90
        
    return amount

amount = int(input("Enter Amount:"))
coupon_code = input("Enter Coupon Code:")
print(apply_coupon(amount, coupon_code))
