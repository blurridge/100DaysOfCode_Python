# Ball

from turtle import Turtle 

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.movement_speed = 0.1
        self.x_dir = 10
        self.y_dir = 10
    
    def move(self):
        x = self.xcor() + self.x_dir
        y = self.ycor() + self.y_dir
        self.setpos(x, y)
    
    def bounce_y(self):
        self.y_dir *= -1
    
    def bounce_x(self):
        self.x_dir *= -1
    
    def reset(self):
        self.setpos(0, 0)
        self.bounce_x()
        self.movement_speed = 0.1
    
    def speed_up(self):
        self.movement_speed*=0.7
    
    def clear(self):
        self.hideturtle()