from turtle import Turtle, Screen
from random import choice

timmy = Turtle()
screen = Screen()

colors = ["yellow", 'red', 'blue', 'coral', 'cyan', 'green', 'purple', 'pink', 'orange', 'black']


def draw_shape(number_of_turns):
    color = choice(colors)
    timmy.color(color)
    angle = 360 / number_of_turns
    for _ in range(number_of_turns):
        timmy.forward(100)
        timmy.right(angle)


for f in range(3, 10):
    draw_shape(f)


