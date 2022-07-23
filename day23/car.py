# Car

from turtle import Turtle 
import random 

CAR_COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
CAR_MOVE_DIS = 5
CAR_MOVE_INCR = 10

class Car():

    def __init__(self):
        self.car_list = list()
        self.move_speed = CAR_MOVE_DIS

    def create_car(self):
        rng = random.randint(1, 6)
        if rng == 6:
            new_car = Turtle()
            new_car.color(random.choice(CAR_COLORS))
            new_car.penup()
            new_car.shape("square")
            new_car.setheading(180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.setpos(300, random_y)
            self.car_list.append(new_car)
    
    def move_car(self):
        for car in self.car_list:
            car.forward(self.move_speed)

    def clear(self):
        for car in self.car_list:
            car.hideturtle()
    
    def increase_speed(self):
        self.move_speed += CAR_MOVE_INCR