def reversed_string(s,rev=""):
    rev=""

    for i in s:
        rev=i+rev

    print("Reversed String:",end=" ")
    return rev

s=input("Enter String:")
print(reversed_string(s))