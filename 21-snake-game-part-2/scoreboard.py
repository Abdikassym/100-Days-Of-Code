from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 250)
        self.color('white')
        self.score = -1
        self.update_score()

    def add_score(self):
        self.score += 1

    def update_score(self):
        self.add_score()
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 16, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over.", False, align="center", font=("Arial", 16, "normal"))
