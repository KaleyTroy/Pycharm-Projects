from turtle import *

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.shape("circle")
        self.penup()
        self.p1_inbounds = 0
        self.p2_inbounds = 0
        self.pace = 5

    def new_ball(self):
        self.showturtle()
        self.setpos(0, 0)
        self.setheading(180 * self.p1_inbounds - 0)
        self.p1_inbounds = 1
        self.p2_inbounds = 1
        self.pace = 5

    def move_ball(self, left_side, right_side):
        self.forward(self.pace)
        self.pace *= 1.001
        direction = int(self.heading())
        if self.xcor() > 335:
            if right_side[0] < self.ycor() < right_side[1]:
                if 0 <= direction < 90:
                    self.setheading(180 - direction - right_side[2] * 3)
                if 270 <= direction < 360:
                    self.setheading(540 - direction - right_side[2] * 3)

        if self.xcor() < -335:
            if left_side[0] < self.ycor() < left_side[1]:
                if 180 <= direction < 270:
                    self.setheading(540 - direction + left_side[2] * 4)
                if 180 > direction >= 90:
                    self.setheading(180 - direction + left_side[2] * 4)

        if self.ycor() < -250:
            if 180 <= direction < 360:
                self.setheading(360 - direction)

        if self.ycor() > 250:
            if 0 <= direction < 180:
                self.setheading(360 - direction)

    def dead_zone(self):
        if self.xcor() < -380:
            self.p1_inbounds = 0
            self.hideturtle()

        if self.xcor() > 380:
            self.p2_inbounds = 0
            self.hideturtle()
