# Main

from turtle import Turtle, Screen
import extract_colors
import random

screen = Screen()
screen.colormode(255)

turtle = Turtle()
turtle.hideturtle()
turtle.penup()
turtle.setposition(-200, -200)
turtle.speed("fastest")
turtle.pensize(20)

colors = extract_colors.get_colors("hirst_image.jpg")

for i in range(0, 10):
    for j in range(0, 10):
        turtle.pendown()
        turtle.dot(20, random.choice(colors))
        turtle.penup()
        turtle.forward(50)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.setposition(-200, turtle.ycor())
    turtle.right(90)
    
screen.exitonclick()