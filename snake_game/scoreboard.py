from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
file = open("text")
file_high_score = file.read()
file.close()

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(file_high_score)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.display()

    def point(self):
        self.score += 1
        self.display()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open("text", "w")
            file.write(str(self.high_score))
            file.close()
        self.score = 0
        self.display()

    def display(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)
