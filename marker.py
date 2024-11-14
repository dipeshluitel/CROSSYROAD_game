from turtle import Turtle


class Mark(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-300, 270)
        self.pendown()
        self. forward(600)
