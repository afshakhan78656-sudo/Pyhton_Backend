celcius=float(input("Enter Weather in Celcuis:"))

if celcius>50:
    print("Invalid")

elif celcius>40 and celcius<=50:
    print("Temprature is too hot!!")

elif celcius>30 and celcius<=40:
    print("Temprature is hot!!")

elif celcius>20 and celcius<=30:
    print("Temprature is noraml!!")

elif celcius>10 and celcius<=20:
    print("Temprature is cold!!")

elif celcius>0 and celcius<=10:
    print("Temprature is too cold!!")

else:
    print("Freeze!!")




