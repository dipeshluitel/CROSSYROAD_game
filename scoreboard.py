from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.color("black")
        self.hideturtle()

    def display_level(self, score):
        self.clear()
        self.goto(-240, 250)
        self.write(f"Level : {self.level}", move=False, align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align='center', font=FONT)

