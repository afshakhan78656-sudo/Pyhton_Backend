# Stone, Paper, Scissor Game using list with random library
import random
lucky=["Stone","Paper","Scissor"]

lucky=random.choice(lucky)

while True:
    print("*********Enter your choice*********")
    choice=input("Enter your choice: ")
    print(lucky)

    if choice==lucky:
      print("Congratulations! You have won the game")
      break

    elif choice=="Stone" and lucky=="Paper":
      print("You have lost the game")
      break

    elif choice=="Paper" and lucky=="Scissor":
      print("You have lost the game")
      break 

    elif choice=="Scissor" and lucky=="Stone":
      print("You have lost the game")
      break