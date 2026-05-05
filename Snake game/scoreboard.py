from turtle import Turtle
FONT = ("courier", 12, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.refresh()


    def increase_score(self):
        self.score += 1

    def refresh(self):
        self.hideturtle()
        self.clear()
        self.goto(0, 275)
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER!", False, ALIGNMENT, FONT)