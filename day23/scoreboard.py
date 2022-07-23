# Scoreboard

from turtle import Turtle

FONT = ("Helvetica", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.setpos(-240, 260)
        self.write_scoreboard()
    
    def write_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", move = False, align = "center", font = FONT)

    def write_game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(f"Game over! You only reached level {self.level}.", move = False, align = "center", font = FONT)
    
    def level_up(self):
        self.level+=1