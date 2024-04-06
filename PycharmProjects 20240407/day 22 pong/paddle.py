from turtle import *
class Paddle(Turtle):

    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("pink")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=5)
        self.setpos(350 * side, 0)
        self.setheading(90)
        self.velocity = 0
        self.hit_box = ()

    def go_up(self):
        if self.ycor() < 220:
            self.velocity = 5
        else:
            self.velocity = 0

    def go_up_release(self):
        self.velocity = 0

    def go_down(self):
        if -220 < self.ycor():
            self.velocity = -5
        else:
            self.velocity = 0

    def go_down_release(self):
        self.velocity = 0

    def move_paddle(self):
        self.forward(self.velocity)
        return self.ycor() - 50, self.ycor() + 50, self.velocity
