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
score = Scoreboard()

screen.listen()
screen.onkeypress(player.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()
    for car in cars.car_list:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    if player.finish_line():
        player.reset_position()
        cars.speed_increase()
        score.increase_level()


screen.exitonclick()
