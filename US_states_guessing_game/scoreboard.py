from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup()
        self.hideturtle()

    def add_point(self):
        self.points += 1

    def print_text(self, x, y, state):
        self.goto(x, y)
        self.write(state)
