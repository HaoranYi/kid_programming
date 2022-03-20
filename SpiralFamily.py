import turtle   #Set up turtle graphiics
t = turtle.Pen()
turtle.bgcolor("black")
colors = ["red", "yellow", "brown", "orange", "purple","pink","green", "blue", "white" ]
family = []        # Set up an empty list for family names
#ask for the first name
name = turtle.textinput("My Family", "Enter a name, or just hit [ENTER] to end:")
#keep asking for names
while name != "":
    #Add their name to the family list
    family.append(name)    
    #Add their name for another name, or end
    name = turtle.textinput("My Family", "Enter a name, or just hit [ENTER] to end:")
# draw a spiral of the names on the screen
for x in range(100) :
    t.pencolor(colors[x%len(family)]) # rotate through the colors
    t.penup()  # dont draw the regular spiral lines
    t.forward(x*4)  # just move the turtle on the screen
    t.pendown()  # draw the next family member's name
    t.write(family[x%len(family)], font = ("indie flower", int((x+4)/4), "bold"))
    t.left(360/len(family) + 2)   # turn left for our spiral