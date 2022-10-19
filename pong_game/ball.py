from turtle import Turtle
SPEED = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed_up = 1
        self.move_x = SPEED
        self.move_y = SPEED

    def movement(self):
        new_x = self.xcor() + self.move_x * self.speed_up
        new_y = self.ycor() + self.move_y * self.speed_up
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def restart(self):
        self.goto(0, 0)

