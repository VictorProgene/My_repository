from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.forward(-10)

def rotate_clockwise():
    tim.right(10)

def rotate_counter_clockwise():
    tim.left(10)

def clear_secreen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
# def turn_right():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)


screen.listen()
screen.onkey(key = "w", fun = move_forwards)
screen.onkey(key = "s", fun = move_backwards)
screen.onkey(key = "a", fun = rotate_clockwise)
screen.onkey(key = "d", fun = rotate_counter_clockwise)
screen.onkey(key = "c", fun = clear_secreen)





screen.exitonclick()