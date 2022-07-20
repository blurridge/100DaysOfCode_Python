# Main

from turtle import Screen 
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by blurridge")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.update()
screen.listen()
screen.onkey(fun = snake.up, key = "Up")
screen.onkey(fun = snake.down, key = "Down")
screen.onkey(fun = snake.left, key = "Left")
screen.onkey(fun = snake.right, key = "Right")

continue_game = True 
while continue_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food) < 15:
        food.move_random()
        snake.extend()
        scoreboard.score+=1
        scoreboard.write_scoreboard()
    
    if snake.wall_collision():
        continue_game = False
        snake.clear()
        food.clear()
        screen.update()
        scoreboard.write_game_over()

    if snake.tail_collision():
        continue_game = False
        snake.clear()
        food.clear()
        screen.update()
        scoreboard.write_game_over()

screen.exitonclick()