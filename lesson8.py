import random
suits = ["clubs", "dimonds", "hearts", "spades"]
faces = ["two", "three", "four", "five", "six","seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
keep_going = True
while keep_going: 
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("OINKK, I have the", my_face,"of", my_suit)
    print("OINKK, You have the", your_face, "of", your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print("OINKK, I Win!")
    elif faces.index(my_face) < faces.index(your_face):
        print("OINKK, You win!")
    else:


        print("It's a tie!")
    answer = input("Hit [Enter] to keep going, any key to exit:")
    keep_going = (answer=="")