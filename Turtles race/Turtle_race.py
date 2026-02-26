import turtle
from turtle import Turtle, Screen
import random

def who_wins():
    global colors
    global user_bet
    positions = []
    for turtle_i in all_turtles:
        winner_position = turtle_i.xcor()
        positions.append(winner_position)
    winner_x = max(positions)
    winner = positions.index(winner_x)

    if colors[winner] == user_bet:
        print(f"You win! The {colors[winner]} turtle wins!")
    else:
        print(f"You lose! The {colors[winner]} turtle wins!")

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make your bet!", prompt = "Which Turtle is going to win? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-240, y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        position = turtle.xcor()
        print(int(position))
        if position >= 240:
            is_race_on = False

who_wins()

screen.exitonclick()