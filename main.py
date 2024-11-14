# TODO: DETECT PLAYER REACHING NEXT SIDE
# TODO: DISPLAY SCORE BOARD AND ADD LEVEL UP FEATURE

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
screen.listen()

screen.onkey(player.upward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on = False

    if player.check_finish():
        player.goto_beginning()
        cars.level_up()

screen.exitonclick()
