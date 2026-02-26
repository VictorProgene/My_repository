import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.color("coral")
tim.speed("fastest")
tim.hideturtle()



tim.pensize(30)

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def tim_random_color():
    rgb = [(187, 164, 126), (220, 215, 114), (131, 168, 190), (139, 88, 62), (52, 108, 145), (138, 177, 147), (188, 144, 153), (141, 71, 85), (156, 161, 53), (47, 35, 24), (138, 23, 38), (62, 117, 76), (19, 39, 66), (76, 20, 28), (176, 96, 112), (86, 157, 101), (185, 100, 81), (25, 48, 33), (57, 154, 183), (21, 60, 116), (216, 176, 183), (216, 179, 174), (172, 204, 177), (120, 36, 31), (27, 91, 50), (70, 73, 35)]
    random_rgb = random.choice(rgb)
    tim.pencolor(random_rgb)

def random_direction():
    direction = random.choice(["left", "right"])
    angle = random.choice([0, 90, 180, 270])
    if direction == "left":
        tim.left(angle)
        tim.forward(50)
    else:
        tim.right(angle)
        tim.forward(50)

def change_lane():
    global position
    position +=  54


# -----------------------------------------------------------------------------

position = -270


while position < 270:

    change_lane()
    tim.penup()
    tim.goto(-300, position)
    tim.pendown()

    for _ in range(10):
        tim_random_color()
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(65)

    if position >= 270:
        print("Done")








screen = Screen()
screen.exitonclick()