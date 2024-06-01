from turtle import Turtle


class Pad(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.shape("square")
        self.goto(x, y)
        self.setheading(90)

    def move_up(self):
        self.forward(20)

    def move_down(self):
        self.backward(20)
