import logging
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from time import sleep
from net import Net
from scoreboard import Scoreboard

logging.basicConfig(level = logging.DEBUG)

y_pos = 160

scr = Screen()
scr.title("Pong")
scr.bgcolor("black")
scr.setup(width = 800, height = 600)
scr.tracer(0)

pad1 = Paddle(350)
pad2 = Paddle(-360)
ball = Ball()
net = Net()
scoreboard = Scoreboard()

game_started = True

scr.listen()
scr.onkey(pad1.go_up, "Up")
scr.onkey(pad1.go_down, "Down")
scr.onkey(pad2.go_up, "a")
scr.onkey(pad2.go_down, "z")

while game_started:
    sleep(ball.move_speed)
    scr.update()
    ball.move()

    # check if ball hitting top/bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # check if ball hits the paddle
    if ball.distance(pad1) < 50 and ball.xcor() > 320 or \
            ball.distance(pad2) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # check for miss (right player)
    if ball.xcor() > 380:
        ball.bounce_x()
        ball.restore()
        scoreboard.update(1, 0)

    # check for miss (left player)
    if ball.xcor() < -380:
        ball.bounce_x()
        ball.restore()
        scoreboard.update(0, 1)


scr.exitonclick()

# logging.debug(stuff)
