from turtle import Turtle


class TurtleTally(Turtle):

    def __init__(self):
        super().__init__()
        self.yummy_turtles = 0
        self.color("pink")
        self.penup()
        self.goto(0, 270)
        self.clear()

    def willies_turtles(self, yum_yums):
        self.clear()
        self.yummy_turtles = yum_yums
        self.write(f"Yummy yummy turtles! {self.yummy_turtles}", align="center", font=("bauhaus", 20, "normal"))
