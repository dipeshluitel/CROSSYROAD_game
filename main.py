import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from marker import Mark
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
screen.listen()
score = Scoreboard()
# marks the finish line
mark_finish_line = Mark()

screen.onkey(player.upward, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    score.display_level(score.level)
    cars.generate_car()
    cars.move_car()

    for car in cars.all_cars:
        if car.distance(player) < 25:
            score.game_over()
            game_is_on = False

    if player.check_finish():
        player.goto_beginning()
        cars.level_up()
        score.level = score.level + 1

screen.exitonclick()
