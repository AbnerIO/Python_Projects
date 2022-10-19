from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

ball = Ball()
scoreboard = Scoreboard()


player1 = Paddle(1)
player2 = Paddle(2)
screen.onkey(player1.up, "Up")
screen.onkey(player2.up, "w")
screen.onkey(player1.down, "Down")
screen.onkey(player2.down, "s")

game_on = True

while game_on:
    time.sleep(.01)
    ball.movement()
    screen.update()
    # Detect coalition with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect coalition with the paddle
    if ball.distance(player2) < 50 and ball.xcor() < 330 or ball.distance(player1) < 50 and ball.xcor() > -330:
        ball.bounce_x()
        ball.speed_up += .1
    if ball.xcor() > 380:
        ball.speed_up = 1
        scoreboard.score_1 += 1
        ball.restart()
        scoreboard.update_scoreboard()
    if ball.xcor() < -380:
        ball.speed_up = 1
        scoreboard.score_2 += 1
        ball.restart()
        scoreboard.update_scoreboard()
screen.exitonclick()
