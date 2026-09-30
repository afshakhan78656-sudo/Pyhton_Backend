def mask_phone_number(phone) :
    return "*******" + phone[-4:]

phone_number = input("Enter your phone number: ")
print(mask_phone_number(phone_number))