# Scoreboard

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 240)
        self.write_scoreboard()
    
    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", move = False, align = "center", font = ("Helvetica", 24, "normal"))

    def write_game_over(self):
        self.clear()
        self.setpos(0, 0)
        self.write(f"Game Over! Your score is {self.score}", move = False, align = "center", font = ("Helvetica", 24, "normal"))