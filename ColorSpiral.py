import turtle
t = turtle.Pen()
turtle.bgcolor('yellow')
sides = 6
colors =["blue", "pink", "green","purple","orange","red"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x *3/sides + x)
    t.left(360/sides +1)
    t.width(x*sides/200)