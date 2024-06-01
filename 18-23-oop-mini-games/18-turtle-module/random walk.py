from turtle import Turtle, colormode
from random import choice, randint

timmy = Turtle()

timmy.width(10)
timmy.speed(10)

colormode(255)

directions = [0, 90, 180, 270]


def move_and_turn():
    r_color = randint(1, 255)
    g_color = randint(1, 255)
    b_color = randint(1, 255)

    timmy.pencolor(r_color, g_color, b_color)
    timmy.forward(30)
    timmy.setheading(choice(directions))
    move_and_turn()


move_and_turn()
