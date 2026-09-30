celsius=float(input("Enter the Temprature in celsisus:"))

if(celsius>50):
    print("Invalid.")

elif(celsius>40 and celsius<=50):
    print(" Temprature is Too Hot")

elif(celsius>30 and celsius<=40):
    print(" Temprature is Hot")

elif(celsius>20 and celsius<=30):
    print(" Temprature is Normal")

elif(celsius>10 and celsius<=20):
    print(" Temprature is cold")

elif(celsius>0 and celsius<=10):
    print(" Temprature is too cold")

else:
    print("Freeze")
