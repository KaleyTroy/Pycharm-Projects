from ball import *
from paddle import *
from scoreboard import *
from time import *
# <editor-fold desc="Screen Settings">
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)
# </editor-fold>
# <editor-fold desc="Variables">
game = True
ball = Ball()
right_paddle = Paddle(1)
left_paddle = Paddle(-1)
score_board = ScoreBoard()
# </editor-fold>
# <editor-fold desc="Keymap">
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeyrelease(right_paddle.go_up_release, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeyrelease(right_paddle.go_down_release, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeyrelease(left_paddle.go_up_release, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeyrelease(left_paddle.go_down_release, "s")
# </editor-fold>
while game:
    ball.new_ball()
    while ball.p1_inbounds and ball.p2_inbounds:
        sleep(1/120)
        ball.move_ball(left_paddle.move_paddle(), right_paddle.move_paddle())
        screen.update()
        ball.dead_zone()
        screen.update()
    score_board.out(ball.p1_inbounds, ball.p2_inbounds)


screen.exitonclick()
