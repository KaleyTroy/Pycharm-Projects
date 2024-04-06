from turtle import *
from math import sin, pi

class DivineTurtle(Turtle):

    def __init__(self,):
        super().__init__()
        self.steps = self.steps_calc()
        self.length = 100 * sin(pi / self.sides[0])
        self.length *= (1 + self.steps // 180)
        self.shape("turtle")
        self.pencolor("gold")
        # self.hideturtle()

    def draw(self, spin, sides, offset, length):
        self.penup()
        for x in range(self.steps):
            self.forward(self.offset)
            self.left(spin)

            self.pendown()
            self.forward(self.length / 2)
            for y in range(self.sides[0] - 1):
                self.right(360 / self.sides[0])
                self.forward(self.length / 2)

            self.penup()
            self.left(90)
            self.forward(self.offset)
            self.right(180)
            self.right(self.increments)

    def steps_calc(self):
        steps = 0
        while self.facing % 360 or self.facing == 0:
            self.facing += self.increments
            steps += 1
        return steps
