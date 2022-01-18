import time
from turtle import Screen, Turtle

from Ball import Ball
from Paddle import Paddle

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")

screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")


game_in_on = True

while game_in_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    # paddle_hit_ball
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Ball is out
    if ball.xcor() > 380:
        time.sleep(1)
        ball.reset_position()
        scoreboard.l_point()
    if ball.xcor() < -380:
        print("score")
        time.sleep(1)
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
