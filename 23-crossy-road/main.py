from turtle import Screen
from player import Player
from car import Car
import time

screen = Screen()
screen.listen()
screen.tracer(0)

player = Player()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")

game_is_on = True

cars = []
for car_enemy in range(10):
    car = Car()
    cars.append(car)

while game_is_on:
    screen.update()
    for i in cars:
        i.move()
        i.respawn()
    time.sleep(0.5)

screen.exitonclick()