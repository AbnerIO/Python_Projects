import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard


# Screen things
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# DO not update the image of the screen
screen.tracer(0)
# Snake things
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
# Food things
food = Food()
# Scoreboard things
scoreboard = Scoreboard()


is_on = True

while is_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Detect coalition with food
    if snake.head.distance(food) < 15:
        scoreboard.point()
        food.refresh()
        snake.extend()
    # Detect coalition with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    # Detect coalition with head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()

screen.exitonclick()
