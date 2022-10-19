from turtle import Turtle
SPEED = 20

class Paddle(Turtle):

    def __init__(self, player):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.choose_position(player)

    def choose_position(self, player):
        if player == 1:
            self.goto(-350, 0)
        elif player == 2:
            self.goto(350, 0)

    def up(self):
        new_y_position = self.ycor() + SPEED
        self.goto(self.xcor(), new_y_position)

    def down(self):
        new_y_position = self.ycor() - SPEED
        self.goto(self.xcor(), new_y_position)








