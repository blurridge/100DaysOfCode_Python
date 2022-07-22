# Paddle

from turtle import Turtle 
MAX_Y = 260
MIN_Y = -260

class Paddle(Turtle):
    
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.orig_x = x_pos
        self.orig_y = y_pos
        self.setpos(x=x_pos, y=y_pos)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
    
    def move_up(self):
        y = self.ycor() + 20
        if y <= MAX_Y:
            self.setpos(self.xcor(), y)
    
    def move_down(self):
        y = self.ycor() - 20
        if y >= MIN_Y:
            self.setpos(self.xcor(), y)

    def reset(self):
        self.setpos(self.orig_x, self.orig_y)

    def clear(self):
        self.hideturtle()