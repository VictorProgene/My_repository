# from turtle import Screen, Turtle
#
# SNAKE_POSITION_X = [0, -20, -40]
# MOVE_DISTANCE = 20
#
# is_race_on = True
# screen = Screen()
# class Snake:
#
#     def __init__(self):
#         self.snake_body = []
#         self.create_snake()
#         self.head = self.snake_body[0]
#
#
#     def create_snake(self):
#
#         for snakes in range(0, 3):
#             self.add_segment(snakes)
#
#     def add_segment(self, snakes):
#         snake = Turtle("square")
#         snake.penup()
#         snake.color("white")
#         snake.goto(x=SNAKE_POSITION_X[snakes], y=0)
#         self.snake_body.append(snake)
#
#     def extend(self):
#         self.add_segment()
#
#     def move(self):
#
#         for seg_num in range(len(self.snake_body) - 1, 0, -1):
#             new_x = self.snake_body[seg_num - 1].xcor()
#             new_y = self.snake_body[seg_num - 1].ycor()
#             self.snake_body[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
#
#     def up(self):
#             if self.head.heading() != 270:
#                 self.head.setheading(90)
#
#     def down(self):
#             if self.head.heading() != 90:
#                 self.head.setheading(270)
#
#     def right(self):
#             if self.head.heading() != 180:
#                 self.head.setheading(0)
#
#     def left(self):
#             if self.head.heading() != 0:
#                 self.head.setheading(180)
#

from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
