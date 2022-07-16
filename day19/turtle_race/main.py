# Main

from turtle import Turtle, Screen
import random

race_start = False
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the color of the turtle that you think will win the race: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
racers = list()
starting_y = -60
winner = None

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(-240, starting_y)
    racers.append(new_turtle)
    starting_y+=30

if user_bet:
    race_start = True

while race_start:
    for turtle in racers:
        new_distance = random.randint(0, 10)
        turtle.forward(new_distance)
        if(turtle.xcor() >= 230):
            race_start = False
            winner = (turtle.color())[0]

if winner == user_bet:
    print("You have won the bet!")
else:
    print(f"You lost! {winner} won!")

screen.exitonclick()