import random

lucky=random.randint(1,3)

while True:
    print("*********Enter your choice*********")
    print("1. Stone")
    print("2. Paper")
    print("3. Scissor")
    
    choice=int(input("Enter your choice: "))
    
    if choice>3:
        print("Please enter a number between 1 to 3")
        
    elif choice==lucky:
        print("It's a tie! Both choose the same.")
        break
    
    elif (choice==1 and lucky==3) or (choice==2 and lucky==1) or (choice==3 and lucky==2):
        print("Congratulations! You have won the game.")
        break
    else:
        print("Sorry! You have lost the game. Better luck next time.")
        break