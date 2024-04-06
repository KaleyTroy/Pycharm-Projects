import time
from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.p1_scoreboard = (-100, -280)
        self.p2_scoreboard = (-100, 280)
        self.pencolor("pink")
        self.sb_write("Welcome to Pong!", 50, 0, 0)

    def sb_print(self, text, size, pos_x, pos_y):
        self.setposition(pos_x, pos_y)
        self.write(text, False, "center", ("courier", size, "normal"))

    def sb_write(self, text, size, pos_x, pos_y):
        self.sb_print(text, size, pos_x, pos_y)
        time.sleep(1)
        self.clear()
        self.sb_print(self.p1_score, 30, -100, 250)
        self.sb_print(self.p2_score, 30, 100, 250)

    def out(self, p1, p2):
        self.sb_write("Out!", 50, 0, 0)
        if p1:
            self.p1_score += 1
            self.sb_write("Player 1 wins!", 50, 0, 0)
            self.sb_write("Player 2 serves", 50, 0, 0)
        if p2:
            self.p2_score += 1
            self.sb_write("Player 2 wins!", 50, 0, 0)
            self.sb_write("Player 2 serves", 50, 0, 0)
