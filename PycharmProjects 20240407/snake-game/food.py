from random import randint
from turtle import Turtle


class ALittleSnackForWillie(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("blue")
        self.fillcolor("green")
        self.shapesize(1)
        self.penup()
        self.setpos(randint(-55, 55) * 5, randint(-55, 55) * 5)
        self.more_turtles()

    def more_turtles(self):
        self.goto(randint(-59, 59) * 5, randint(-59, 59) * 5)

