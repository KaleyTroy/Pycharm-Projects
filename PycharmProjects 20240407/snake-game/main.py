from time import sleep
from turtle import Screen
from snakebody import WillieTheSnake
from food import ALittleSnackForWillie
from scoreboard import TurtleTally

for screen_start in [1]:
    RIGHT, LEFT, DOWN, UP = 0, 180, 90, 270
    willie_pad = Screen()
    willie_pad.tracer(0)
    willie_pad.setup(width=600, height=600, startx=0, starty=0)
    willie_pad.bgcolor("black")
    willie_pad.title("Esta's art of love and abundance")
    willie_pad.listen()
for willie_grow in [1]:
    willie = WillieTheSnake(40)
    willie_snack = ALittleSnackForWillie()
    willie_pad.listen()
    willie_pad.onkey(willie.right, "d")
    willie_pad.onkey(willie.up, "w")
    willie_pad.onkey(willie.left, "a")
    willie_pad.onkey(willie.down, "s")
    willie_pad.update()
    t = -500
for turtles in [1]:
    turtle_tally = TurtleTally()
    turtle_tally.willies_turtles(len(willie.willie_shaft))

while willie.alive:
    willie.thrust_willie()
    willie_pad.update()
    sleep(willie.speed**-1)
    if willie.willie_head.distance(willie_snack) < 10:
        willie_snack.more_turtles()
        willie.fresh_willie(10)
        turtle_tally.willies_turtles(len(willie.willie_shaft))
    for x in willie.willie_shaft[5:]:
        if willie.willie_head.distance(x) < 10:
            willie.alive = False
            print("dicks")



willie_pad.exitonclick()

