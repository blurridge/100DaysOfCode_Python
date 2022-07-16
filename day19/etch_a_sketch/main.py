# Main

from turtle import Turtle, Screen
import movement

screen = Screen()

screen.listen()
screen.onkey(key="Up", fun=movement.move_forwards)
screen.onkey(key="Down", fun=movement.move_backwards)
screen.onkey(key="Left", fun=movement.move_counterclock)
screen.onkey(key="Right", fun=movement.move_clockwise)
screen.onkey(key="c", fun=movement.clear_screen)

screen.exitonclick()