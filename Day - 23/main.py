from turtle import Screen,Turtle
import time
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height= 600, width=600)
screen.tracer(0)

player = Player()
cars = CarManager()
score = ScoreBoard()

screen.listen()
screen.onkey(player.move_up,"Up")

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()
#   Detect collison of turtle
    for car in cars.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            score.game_over()

    if player.is_finished():
        player.go_to_start()
        cars.level_up()
        score.increase_lvl()


screen.exitonclick()