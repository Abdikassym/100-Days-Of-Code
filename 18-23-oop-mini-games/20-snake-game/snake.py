from turtle import Turtle


class Snake:
    def __init__(self):
        self.all_segments = []
        segment_position = [(0, 0), (-20, 0), (-40, 0)]

        for position in segment_position:
            turtle_segment = Turtle()
            turtle_segment.color('white')
            turtle_segment.shape("square")
            turtle_segment.penup()
            turtle_segment.goto(position)
            self.all_segments.append(turtle_segment)

        self.head = self.all_segments[0]

    def move(self):
        for seg in range(len(self.all_segments) - 1, 0, -1):
            new_x = self.all_segments[seg - 1].xcor()
            new_y = self.all_segments[seg - 1].ycor()
            self.all_segments[seg].goto(new_x, new_y)
        self.all_segments[0].forward(20)

    def current_heading(self):
        return self.head.heading()

    def up(self):
        if self.current_heading() == 270:
            return
        else:
            self.head.setheading(90)

    def down(self):
        if self.current_heading() == 90:
            return
        else:
            self.head.setheading(270)

    def left(self):
        if self.current_heading() == 0:
            return
        else:
            self.head.setheading(180)

    def right(self):
        if self.current_heading() == 180:
            return
        else:
            self.head.setheading(0)
