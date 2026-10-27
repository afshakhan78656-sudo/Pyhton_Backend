class InvalidCouponCodeError(Exception):
    pass


valid_codes = ["SAVE10", "FOOD20", "WELCOME"]

coupon = input("Enter coupon code: ")

try:
    if coupon not in valid_codes:
        raise InvalidCouponCodeError

    print("Coupon applied successfully!")

except InvalidCouponCodeError:
    print("Invalid coupon code!")