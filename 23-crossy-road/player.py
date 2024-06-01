from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.goto(0, -180)
        self.shape("turtle")
        self.color("black")

    def up(self):
        self.setheading(90)
        self.forward(10)

    def down(self):
        self.setheading(270)
        self.forward(10)

    def left(self):
        self.setheading(180)
        self.forward(10)

    def right(self):
        self.setheading(0)
        self.forward(10)