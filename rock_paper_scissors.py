import random
from time import sleep

choice = ["Rock", "Paper", "Scissors"]
computer = random.choice(choice)
#print("The computer has chosen : ", computer)

player = False

while player == False:
    print("Welcome to Rock,Paper and Scissors!")
    print("\nPlease, wait the game is loading....")
    sleep(3)
    player = input("Which one do you want to choose?\n'Rock': 'Rock'\n'Paper': 'Paper'\n'Scissors': 'Scissors'\n'Stop the game': 'Stop': ")
    if player == computer:
        print("\nPlease wait we are loading your results...")
        sleep(2)
        print("Its a Tie !!")
        print("The computer has also chosen :", computer)
    elif player == "Rock":
        if computer == "Paper":
            print("\nPlease wait we are loading your results...")
            sleep(2)
            print("You have Lost !, The computer has chosen Paper")
        else:
            print("\nPlease wait we are loading your results...")
            sleep(2)
            print("You have Won !!!")
            print("\n The computer has chosen :", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("\nPlease wait we are loading your results...")
            sleep(2)
            print("You have Lost !, The computer has chosen Rock")
        else:
            print("\nPlease wait we are loading your results...")
            sleep(2)
            print("You have Won !!!")
            print("\n The computer has chosen :", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("\nPlease wait we are loading your results...")
            sleep(2)
            print("You have Lost !, The Computer has chosen scissors")
        else:
            print("\nPlease wait we are loading your results...")
            sleep(2)
            print("You have Won !!!")
            print("\n The computer has chosen :", computer)
    elif player == "Stop":
        print("Thanks for Playing !!")
        break
    else:
        print("That's not a valid play !!")
        break

    player = False
# By: Raji




