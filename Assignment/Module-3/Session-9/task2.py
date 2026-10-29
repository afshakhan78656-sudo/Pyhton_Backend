import re

text = input("Enter text: ")

mobile = re.search(r"\b[0-9]{10}\b", text)

if mobile:
    print("Mobile Number:", mobile.group())
else:
    print("Mobile number not found")