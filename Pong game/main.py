from turtle import Screen
from scoreboard import Scoreboard
from paddles import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

scoreboard = Scoreboard()
paddle_right = Paddle((370, 20))
paddle_left = Paddle((-370, 20))
ball = Ball()

screen.listen()
screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision with the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with the r_paddle
    if (ball.distance(paddle_right) < 50 and ball.xcor() > 320) or (ball.distance(paddle_left) < 50 and ball.xcor() < -320):
        ball.bounce_x()
    # Detect if paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_score_left()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_score_right()





    scoreboard.refresh()































screen.exitonclick()