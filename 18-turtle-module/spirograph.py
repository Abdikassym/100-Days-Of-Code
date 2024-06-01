import turtle
from turtle import Turtle, colormode
from random import choice, randint

timmy = Turtle()

timmy.speed(100)

colormode(255)


def change_color():
    r_color = randint(1, 255)
    g_color = randint(1, 255)
    b_color = randint(1, 255)
    print(type(timmy.pencolor(r_color, g_color, b_color)))
    return timmy.pencolor(r_color, g_color, b_color)


def draw_circle(turn_rate):
    for i in range(int(360 / turn_rate)):
        change_color()
        timmy.circle(100)
        timmy.left(5)


draw_circle(5)
