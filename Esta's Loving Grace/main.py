from time import *
from divine_turtle import *
from math import sin, pi
from turtle import *

screen = Screen()
screen.tracer(1)
screen.bgcolor("black")
screen.setup(1920, 1080, 0, -1)
draw = DivineTurtle()


while True:
    for a in range(360):
        draw.draw(90, 1)
        screen.update()
        sleep(1/1000)
        draw.clear()

screen.exitonclick()
