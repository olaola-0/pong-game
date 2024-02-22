from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

right_pad = Paddle((350, 0))
left_pad = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(right_pad.go_up, "Up")
screen.onkeypress(right_pad.go_down, "Down")
screen.onkeypress(left_pad.go_up, "w")
screen.onkeypress(left_pad.go_down, "s")


def check_collision(bb1, bb2):
    x1, y1, x2, y2 = bb1  # unpack the bounding box of the first object (ball)
    x3, y3, x4, y4 = bb2  # unpack the bounding box of the second object (paddle)
    # check if the x and y coordinates of the bounding boxes overlap
    if (x1 <= x4 and x2 >= x3) and (y1 >= y4 and y2 <= y3):
        return True
    else:
        return False


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect Collision with the Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    if check_collision(ball.bounding_box(), right_pad.bounding_box()):
        ball.bounce_x()
    elif check_collision(ball.bounding_box(), left_pad.bounding_box()):
        ball.bounce_x()

    # Detect Right Paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect Left Paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
