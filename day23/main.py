# Main 

from turtle import Screen 
from player import Player 
from car import Car 
from scoreboard import Scoreboard
import time 

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.title("Turtle Crossing Game by blurridge")

continue_game = True
cars = Car()

while continue_game:
    time.sleep(0.1)
    screen.update()
    score.write_scoreboard()
    cars.create_car()
    cars.move_car()

    for car in cars.car_list:
        if player.distance(car) < 25:
            continue_game = False
            player.car_collision()
            player.clear()
            cars.clear()
            screen.update()
            score.write_game_over()

    if player.ycor() == 300:
        player.player_win()
        cars.increase_speed()
        score.level_up()

screen.exitonclick()