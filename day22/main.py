# Main

from turtle import Screen 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

MAX_SCORE = 2

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong by blurridge")
screen.tracer(0)

player_one = Paddle(-350, 0)
player_two = Paddle(350, 0)
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(key="w", fun=player_one.move_up)
screen.onkey(key="s", fun=player_one.move_down)
screen.onkey(key="Up", fun=player_two.move_up)
screen.onkey(key="Down", fun=player_two.move_down)

continue_game = True
while continue_game:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()
    score.write_scoreboard()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if (ball.distance(player_two) < 50 and ball.xcor() > 320) or (ball.distance(player_one) < 50 and ball.xcor() < -320):
        ball.bounce_y()
        ball.bounce_x()
        ball.speed_up()
    
    if ball.xcor() > 380:
        score.one_score+=1
        score.write_scoreboard()
        screen.update()
        ball.reset()
        player_one.reset()
        player_two.reset()
        time.sleep(1)

    if ball.xcor() < -380:
        score.two_score+=1
        score.write_scoreboard()
        screen.update()
        ball.reset()
        player_one.reset()
        player_two.reset()
        time.sleep(1)
    
    if score.one_score == MAX_SCORE or score.two_score == MAX_SCORE:
        continue_game = False 
        player_one.clear()
        player_two.clear()
        ball.clear()
        screen.update()
        score.write_winner()

screen.exitonclick()