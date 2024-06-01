from turtle import Turtle, Screen
from random import randint

screen = Screen()

HEIGHT = 400
WIDTH = 500

screen.setup(WIDTH, HEIGHT)
user_input = screen.textinput("Make your bet", "Which turtle will win the race? ")

colors = ['red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'purple']

turtles = []
# tim = Turtle('turtle')

# tim.penup()
# tim.goto(-200, -100)

start_x = -230
start_y = -100

for i in range(0, 7):
    turtle = Turtle('turtle')
    turtle.color(colors[i])
    turtle.penup()
    turtles.append(turtle)
    turtle.goto(start_x, start_y)
    start_y += 30

if user_input:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() >= 240:
            race_is_on = False
            print(f"{turtle.color()[0]} turtle won!")

            if turtle.color()[0] == user_input:
                print("You bet is correct!")
            else:
                print("You were wrong!")

screen.exitonclick()
