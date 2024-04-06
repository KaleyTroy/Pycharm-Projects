import random
from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape("turtle")

my_screen = Screen()
print(my_screen.canvheight)
timmy.shapesize(10)
timmy.color("pink")
print(my_screen.canvwidth)
z = (200, 150)

q = True
while q:
    timmy.forward(random.randint(0, 360))
    timmy.left(random.randint(0, 360))
    # print(timmy.position())
    if not 0 < z[0] < 400:
        z = (200, z[1])
    if not 0 < z[1] < 300:
        z = (z[0], 150)
    timmy.position = z
    if z == 999:
        q = False

my_screen.exitonclick()
