print ( "MathHomework.py")
problem = input ("Enter a math problem here, or 'poop' to quit: ")
while (problem != "poop"):
    print ( "The answer to ", problem, "is:", eval(problem))
    problem= input ("Enter another math problem, or 'poop' to quit:")