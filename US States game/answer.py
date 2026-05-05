from turtle import Turtle
FONT = ("courier new", 10, "bold")
ALIGNMENT = "center"

class Answer(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.final_answer = ""
        self.answer_x = 0
        self.answer_y = 0

    def check_answer(self, answer, x, y):
        new_answer = Turtle() #Create new Turtle
        new_answer.penup()
        self.final_answer = answer
        self.answer_x = x
        self.answer_y = y
        new_answer.hideturtle()
        new_answer.clear()
        new_answer.goto(self.answer_x, self.answer_y)
        new_answer.write(f"{self.final_answer}", False, ALIGNMENT, FONT)





