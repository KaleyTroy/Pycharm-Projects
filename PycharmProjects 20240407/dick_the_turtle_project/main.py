import turtle
from random import randint
dick = turtle.Turtle(shape="turtle")
dick_pad = turtle.Screen()
dick.shapesize(8)
dick_pad.setup(width=1540, height=900, startx=3734, starty=-700)
dick_pad.colormode(255)
dick_pad.bgcolor(0, 0, 0)
# dick.pencolor(200, 200, 100)
# dick.penup()
# dick.goto(x=-650, y=300)
colr = "red,yellow,green,magenta,blue,cyan".split(",")

print(colr[0])
willi = []
for j, i in enumerate(colr):
    willi.append(turtle.Turtle(shape="turtle"))
    willi[j].shapesize(6)
    willi[j].fillcolor(i)
    willi[j].goto(x=-650, y=300 - 100 * j)

winner = 0
while not winner:
    for j, i in enumerate(willi):
        willi[j].forward(randint(0, 10))
        if willi[j].xcor() > 500:
            winner = j
print(f"...and the winner is... Number {winner + 1}! The {colr[winner].capitalize()} turtle!")
dick_pad.exitonclick()
