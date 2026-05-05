from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self, initial_pos):
        super().__init__()
        self.new_paddle = Turtle("square")
        self.new_paddle.shapesize(5, 1)
        self.new_paddle.hideturtle()
        self.new_paddle.showturtle()
        self.new_paddle.color("white")
        self.new_paddle.penup()
        self.new_paddle.goto(initial_pos)

    def go_up(self):
        y = self.new_paddle.ycor()
        self.new_paddle.sety(y + MOVE_DISTANCE)

    def go_down(self):
        y = self.new_paddle.ycor()
        self.new_paddle.sety(y - MOVE_DISTANCE)


