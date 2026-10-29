import re

email = input("Enter Gmail: ")

if re.match(r"^[a-z].*@gmail\.com$", email):
    print("Valid Gmail")
else:
    print("Invalid Gmail")