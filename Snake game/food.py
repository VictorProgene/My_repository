from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.refresh()

    def refresh(self):
        self.x = random.randint(-280,280)
        self.y = random.randint(-280,260)
        self.goto(self.x,self.y)