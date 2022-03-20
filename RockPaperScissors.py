import random
choices = ["rock", "paper", "scissors"]
print("Rock crushes scissors. Scissors cute paper. Paper covers rock.")
player = input("Do you want to be rock, paper, or scissors (or quit)?")
while player!= "quit":
    player = player.lower()
    computer = random.choice(choices)
    print("You chose" +player+", and the computer chose" +computer+".")
    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("YAY YOUR MOMA IS GLAD !!!")
        else:
            print("O NOOOOO")
    elif player == "paper":
        if computer == "rock":
            print("THE SQIRRELS ARE VERY HAPPY")
        else:
            print("THE SQIRRELS HATE YOU AND ARE ATTAKING YOU, HIDE!")
    elif player == "scissors":
            if computer == "paper":
                print("YAY YOUR MOMA IS GLAD:)")
            else:
                print("OH NO...you moma is gonna come for you, run")
    else:
        print("We are experiancing an error right now, please try again later")
    print()
    player = input("Do you want to be rock, paper, or scissors (or quit)?")