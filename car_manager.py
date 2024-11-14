from turtle import Turtle
from random import randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        chance = randint(1, 6)
        if chance == 6:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shape('square')
            y_cor = randint(-200, 200)
            new_car.goto(300, y_cor)
            new_car.shapesize(stretch_len=2)
            new_car.color(COLORS[randint(0, 5)])
            new_car.color(COLORS[randint(0, 5)])
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
