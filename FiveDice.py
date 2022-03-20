import random
# Game Loop
keep_going = True
while keep_going:
    #"Roll" 5 random dice
    dice = [0, 0, 0, 0, 0]
    for i in range (5):
        dice[i] = random.randint(1,6)
    print("you rolled:", dice)
    dice.sort()
    if dice[0] == dice[4]:
        print("YANHTZEE PIGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG")
    elif (dice[0] == dice[3]) or (dice[1] == dice[4]):
        print("OINKKKKKKKKK Four of a kind!!!!")
    elif (dice[0] == dice[2]) or (dice[1] == dice[3]) or (dice[2] == dice[4]):
        print("SKIRRRRRRRRRRRRRRRRTTTT Three of a kind")
    keep_going = (input("Hit [Enter] to keep going, any key to exit:") =="")