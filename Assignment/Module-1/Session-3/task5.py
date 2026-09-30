n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
operator=input("Enter Operators(+,-,*,/):")

if operator == "+":
    print("Addition is:",n1+n2)

elif operator == "-":
    print("Substraction is:",n1-n2)

elif operator == "*":
    print("Multiplicatio is:",n1*n2)

elif operator == "/":
    print("Division is:",n1/n2)

else:
    print("Invalid Operator!!")