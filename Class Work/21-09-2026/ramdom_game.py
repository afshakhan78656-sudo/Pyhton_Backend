 #random number deta hai jaise opt, lucky draw etc
'''

import random
lucky=random.randint(1,51)

l=[56446764,547647,3566363,6567576]
lucky=random.choice(l)
print(lucky)
'''
import random
lucky =random.randint(1,50)

while True:
    print("************** Enter Number betwee 1 to 50 ***************")

    choice = int(input("Enter Number:"))

    if choice>50:
        print("Invalid NUmber!!")
        break

    elif choice==lucky:
        print("Congrats!!")
        break

    elif lucky>choice:
        print("Original number is bigger!!")
        
    else:
        print("Original number is lesser!!")