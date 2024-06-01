import time
from turtle import Screen
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()















screen.exitonclick()
