# File: IfSpiral.py
# Author: Charles.y.lee
# Date: 2018-11-11

answer = input("Do you want to see a spiral? y/n:")
if answer=='yes':
    print('working...')
    import turtle
    t=turtle.Pen()
    t.width(2)
    for x in range (1000):
        t.forward(x*2)
        t.left(89)
        print(x)
print('Okay, we are finished!!!')

