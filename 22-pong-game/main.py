import time
from turtle import Screen, Turtle
from pad import Pad
from ball import Ball

screen = Screen()
screen.setup(620, 400)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
game_is_on = True

positions = [(-280, 0), (270, 0)]
pads = []

for position in positions:
    pad = Pad(position[0], position[1])
    pads.append(pad)

player_1 = pads[0]
player_2 = pads[1]
ball = Ball()

screen.onkeypress(player_1.move_up, "w")
screen.onkeypress(player_1.move_down, "s")
screen.onkeypress(player_2.move_up, "Up")
screen.onkeypress(player_2.move_down, "Down")

screen.update()


def bounce(pad_number):
    if ball.distance(pad_number) <= 15:
        print("bounce")
        # heading = ball.heading()
        # ball.setheading(heading * -1)


while game_is_on:
    screen.update()
    time.sleep(0.04)
    ball.move()

    # for pad in pads:
    #     ball.pad_bounce(pad)

    if ball.ycor() >= 200 or ball.ycor() <= -200:
        ball.bounce_y()

    if ball.distance(player_2) < 50 and ball.xcor() >= 260:
        ball.bounce_x()

    if ball.distance(player_1) < 50 and ball.xcor() <= -270:
        ball.bounce_x()



screen.exitonclick()
