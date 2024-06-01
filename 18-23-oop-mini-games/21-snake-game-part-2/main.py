import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=575)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
food = Food()
scores = Scoreboard()

game_is_on = True

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.is_collide_with_wall():
        print("end")
        game_is_on = False
        scores.game_over()

    if snake.head.distance(food) <= 15:
        food.respawn()
        scores.update_score()
        snake.add_segment()

    for segment in snake.all_segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scores.game_over()

screen.exitonclick()
