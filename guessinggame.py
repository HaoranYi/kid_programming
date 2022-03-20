import random
the_number = random.randint(1, 100)
guess = int(input("Guess a number bewtween 1 and 100: "))
num_guess = 1
while guess != the_number:
    if guess > the_number:
        print(guess, "was too high, Try again.")
    if guess < the_number:
        print(guess, "was too low, Try again.")
    guess = int(input("Guess Again!"))
    num_guess += 1
print(guess, "YOUR MOMA WAS HAPPY!!!!!!!!", "num_guess=", num_guess)