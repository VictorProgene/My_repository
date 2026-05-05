from turtle import Turtle
FONT = ("courier new", 50, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.color("white")
        self.penup()
        self.speed('fastest')
        self.refresh()

    def increase_score_left(self):
        self.score_left += 1
        self.refresh()

    def increase_score_right(self):
        self.score_right += 1
        self.refresh()

    def refresh(self):
        self.hideturtle()
        self.clear()
        self.goto(0, 230)
        self.write(f"{self.score_left}   {self.score_right}", False, ALIGNMENT, FONT)

