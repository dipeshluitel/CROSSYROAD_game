from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto_beginning()
        self.shape('turtle')
        self.setheading(90)

    def upward(self):
        self.forward(MOVE_DISTANCE)

    def goto_beginning(self):
        self.goto(STARTING_POSITION)

    def check_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
