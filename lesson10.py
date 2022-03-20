import random
import turtle
t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor("black")
def draw_smiley(x,y):
    t.penup()
    t.setpos(x,y)
    t.pendown()
    #head
    t.pencolor("green")
    t.fillcolor("green")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #Left eyeball
    t.setpos(x-15, y+60)
    t.fillcolor("blue")
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #right eyeball
    t.setpos(x+15, y+60)
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #mouth
    t.setpos(x-25, y+40)
    t.pencolor("black")
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)
for n in range(1000000000):
    x= random.randrange (-turtle.window_width()//2,
                         turtle.window_width()//2)
    y= random.randrange(-turtle.window_width()//2,
                        turtle.window_height()//2)
    draw_smiley(x,y)
    