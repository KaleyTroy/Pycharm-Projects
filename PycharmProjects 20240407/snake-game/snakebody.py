from turtle import Turtle
for master_variables in [1]:
    COLOR = "green,pink".split(",")
    RIGHT_LEFT, DOWN_UP = [0, 180], [90, 270]


class WillieTheSnake:
    def __init__(self, speed):
        self.willie_shaft = []
        self.willie_face = []
        self.alive = True
        self.speed = speed
        self.willie_head = Turtle(shape="turtle")
        self.fresh_willie(10)

    def fresh_willie(self, bits=1):
        for x in range(bits):
            self.willie_shaft += [Turtle(shape="square")]
            self.willie_shaft[-1].penup()
            self.willie_shaft[-1].color(COLOR[len(self.willie_shaft) % 2])
            self.willie_shaft[-1].shapesize(.25)
            self.willie_shaft[-1].goto(400, 400)

        for head in [1]:
            self.willie_shaft[0].shape("circle")
            self.willie_shaft[0].shapesize(0.8)
            self.willie_head.penup()
            self.willie_head.color("green")
            self.willie_head.fillcolor("red")
            self.willie_head.shapesize(0.8)

    def thrust_willie(self):
        for x in range(len(self.willie_shaft) - 1, 0, -1):
            self.willie_shaft[x].goto(self.willie_shaft[x - 1].position())
        for x in range(len(self.willie_face)):
            y = self.willie_face.pop()
            if ((y in DOWN_UP and self.willie_head.heading() in RIGHT_LEFT)
                    or (y in RIGHT_LEFT and self.willie_head.heading() in DOWN_UP)):
                self.willie_head.setheading(y)
        self.willie_head.forward(10)
        x, y = self.willie_head.xcor(), self.willie_head.ycor()
        self.willie_head.setpos(-x, y) if abs(x) > 300 else None
        self.willie_head.setpos(x, -y) if abs(y) > 300 else None
        self.willie_shaft[0].setpos(self.willie_head.position())
        self.willie_shaft[0].setheading(self.willie_head.heading())

    def up(self):
        self.willie_face += [DOWN_UP[0]]

    def down(self):
        self.willie_face += [DOWN_UP[1]]

    def left(self):
        self.willie_face += [RIGHT_LEFT[1]]

    def right(self):
        self.willie_face += [RIGHT_LEFT[0]]
