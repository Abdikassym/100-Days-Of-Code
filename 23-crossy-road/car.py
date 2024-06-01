from turtle import Turtle
from random import choice, randint

colors = ['green', 'purple', 'blue', 'red', 'cyan']


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(randint(150, 300), randint(-150, 150))
        self.shape("square")
        self.color(choice(colors))
        self.setheading(180)

    def create_cars(self, car_list, num_of_cars):
        for car in range(num_of_cars):
            car_list.append(self)

    def move(self):
        self.forward(randint(10, 30))

    def respawn(self):
        x_position = self.xcor()
        if x_position < -180:
            self.goto(150, randint(-150, 150))