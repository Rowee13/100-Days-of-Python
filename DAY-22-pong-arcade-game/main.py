from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('PONG ARCADE GAME')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision of the ball with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision of the ball with the r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # detect right paddle misses the ball
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    # detect left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
