# import colorgram
#
# extracted_colors = colorgram.extract("image.jpg", 30)
# rgb_colors = []
#
# for color in extracted_colors:
#     r = color.rgb[0]
#     g = color.rgb[1]
#     b = color.rgb[2]
#     rgb_colors.append((r, g, b))
#
# print(rgb_colors)
from turtle import colormode, Turtle, Screen
from random import choice


colors = [(212, 154, 97), (52, 107, 131), (177, 78, 33), (200, 142, 34), (116, 155, 171), (124, 79, 98),
          (122, 175, 157), (226, 198, 130), (190, 87, 109), (12, 50, 64), (55, 39, 19), (42, 168, 127), (51, 126, 121),
          (198, 122, 142), (167, 21, 30), (224, 93, 79), (244, 163, 160), (38, 32, 34), (3, 25, 25), (80, 147, 168),
          (162, 26, 22), (238, 164, 167), (21, 78, 88), (174, 206, 187), (103, 127, 156), (166, 203, 209)]

start_x = -320
start_y = -320

timmy = Turtle()
timmy.speed(10)
timmy.penup()
timmy.goto(start_x, start_y)
colormode(255)
timmy.hideturtle()


def change_color_and_draw_a_dot():
    timmy.pencolor(choice(colors))
    timmy.dot(20)
    timmy.forward(70)


for column in range(10):
    for row in range(10):
        change_color_and_draw_a_dot()
    start_y += 70
    timmy.goto(start_x, start_y)

screen = Screen()
screen.exitonclick()
