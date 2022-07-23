# Player 

from turtle import Turtle 

START_POS = (0, -280)
PLAYER_MOVE_DIS = 10
GOAL_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.setpos(START_POS)

    def move_up(self):
        self.forward(PLAYER_MOVE_DIS)
    
    def move_down(self):
        self.backward(PLAYER_MOVE_DIS)

    def car_collision(self):
        self.setpos(START_POS)
    
    def clear(self):
        self.hideturtle()
    
    def player_win(self):
        self.setpos(START_POS)