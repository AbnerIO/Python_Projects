from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score_1 = 0
        self.score_2 = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 170)
        self.write(self.score_1, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 170)
        self.write(self.score_2, align="center", font=("Courier", 80, "normal"))
