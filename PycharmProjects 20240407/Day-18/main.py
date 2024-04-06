import random
import turtle
from turtle import Turtle, Screen
flip = -10


def background_cycle():
    global background_red, background_green, background_blue, cycle, flip
    if cycle % 2 == 0:
        background_red += flip
    if cycle % 2 == 0:
        background_green -= flip
    if cycle % 1 == 0:
        background_blue -= flip
    if cycle % 2 == 0:
        flip *= -1
    t = (background_red, background_green, background_blue)
    return t


screen = Screen()
plops = Turtle()
plops.penup()
plops.shape = turtle
travel = 0
screen.colormode(255)
plops.pensize(1)
boobs = 1
# plops.penup()
# plops.left(90)
# plops.forward(200)
# plops.left(270)
# plops.pendown()
travel = 900
turn = 360 / 16
cycle = 70

plops.left(-3)
plops.speed(1000)
plops.width(1)
global background_red
global background_green
global background_blue
up = True
background_red = 0
background_green = 0
background_blue = 0
r = 100
g = 150
b = 50
plops.pencolor(r,g,b)
screen.bgcolor(background_red, background_green, background_blue)

pycle = 1
while travel != 50:
    pycle += 1
    # if cycle < 250:
    #     up = True
    # if cycle > 1000:
    #     up = False
    # if up:
    #     cycle += 1
    # else:
    #     cycle -= 1
    # plops.pencolor(int(cycle/4), int(cycle/4), int(cycle/4))
    if not pycle % 4:
        plops.left(7)
        plops.forward(0)
        # plops.left(15)

        # print(background_red, background_green, background_blue)

    # r = random.randint(0, 5) * 50  # sets random RGB values by 5% increments
    # g = random.randint(0, 5) * 50  # sets random RGB values by 5% increments
    # b = random.randint(0, 5) * 50  # sets random RGB values by 5% increments
    # screen.bgcolor(r, g, b)  # sets random RGB values by 5% increments

    plops.left(turn)
    plops.forward(travel / 2)
    plops.left(turn + 90)
    plops.pendown()
    for _ in range(6):
        plops.forward(travel)
        plops.left(360 / 6)

    plops.penup()
    plops.left(turn)
    plops.forward(travel / 2)
    plops.left(turn)

screen.exitonclick()
