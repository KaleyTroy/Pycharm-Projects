import turtle
import random
dick = turtle.Turtle()
dick_pad = turtle.Screen()
dick_pad.setup(width=1500, height=800, startx=3762, starty=-800)
dick_pad.colormode(255)
dick_pad.bgcolor(0, 0, 0)
dick.pencolor(200,200,100)
dick.penup()


def move_forwards():
    dick.forward(10)


dick_pad.listen()
# dick_pad.onkey(key="space", fun=move_forwards)
dick_pad.onkeypress(key="space", fun=move_forwards())

dick_pad.exitonclick()
