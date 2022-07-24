# Food

from turtle import Turtle
import random 

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.speed("fastest")
        self.move_random()
    
    def move_random(self):
        rand_x = random.uniform(-280, 280)
        rand_y = random.uniform(-280, 280)
        self.setpos(rand_x, rand_y)
    
    def clear(self):
        self.hideturtle()