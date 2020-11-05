import random
from time import sleep

choices = ["Charmander","Squirtle","Bulbasur"]
computer = random.choice(choices)
#print("The choice of computer is :" , computer)

player = False
name = input("Hello, please enter your name: ")

while player == False:

    print(f"Hello, {name} Welcome to Pokemon Battles Game!!")
    player = input("Which pokemon do you want to choose?\n'Charmander': 'Charmander'\n'Squirtle': 'Squirtle'\n'Bulbasur': 'Bulbasur' \n 'Stop game': 'Stop': ")
    #print("test")
    if player == computer:
         print("Its a Tie !!")
    elif player == "Charmander":
         if computer =="Squirtle":
           print("\n Please, wait loading your results...")
           sleep(2)
           print("You Lose!, The computer has chosen :", computer)
         else:
           print("\n Please, wait loading your results...")
           sleep(2)
           print("You Win !, the computer has chosen : ", computer)
    elif player == "Squirtle":
          if computer == "Bulbasur":
           print("\n Please, wait loading your results...")
           sleep(2)
           print("You Lose !!, The computer has chosen:", computer)
          else:
           print("\n Please, wait loading your results...")
           sleep(2)
           print("You Win !!, The computer has chosen : ", computer)
    elif player == "Bulbasur":
          if computer == "Charmender":
              print("\n Please, wait loading your results...")
              sleep(2)
              print("You Loose !!, The computer has chosen : ",computer)
          else:
              print("\n Please, wait loading your results...")
              sleep(2)
              print("You Win !!, The computer has chosen : ", computer)
    elif player== "Stop":
            print("Thanks for Playing !!")
            break
    else:
          print("That's not a valid play !!")
          break

    player = False










