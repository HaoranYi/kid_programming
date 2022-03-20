name = input("what is your name?")
while name !="":
    for x in range(1000):
        print(name, end = " ")
    print()
    name = input("type another name, or just hit [ENTER] to quit: ")
print("Thanks for learning!")