# Movement
 
from turtle import Turtle

user = Turtle()

def move_forwards():
    user.forward(10)

def move_backwards():
    user.backward(10)

def move_counterclock():
    user.setheading(user.heading() - 10)

def move_clockwise():
    user.setheading(user.heading() + 10)

def clear_screen():
    user.reset()