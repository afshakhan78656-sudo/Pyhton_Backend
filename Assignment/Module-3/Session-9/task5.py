import re

def is_valid_pnr(pnr):
    if re.match(r"^[0-9]{10}$", pnr):
        return True
    else:
        return False

pnr = input("Enter PNR number: ")

if is_valid_pnr(pnr):
    print("Valid PNR")
else:
    print("Invalid PNR")