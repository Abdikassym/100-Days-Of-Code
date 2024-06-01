from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

for i in range(100):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen.exitonclick()
