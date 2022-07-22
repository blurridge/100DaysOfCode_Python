# Scoreboard

from turtle import Turtle 

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.one_score = 0
        self.two_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 240)
        self.write_scoreboard()
    
    def write_scoreboard(self):
        self.clear()
        self.write(f"{self.one_score}\t\t{self.two_score}", move = False, align = "center", font = ("Helvetica", 36, "normal"))
    
    def write_winner(self):
        self.clear()
        self.setpos(0, 0)
        winner = "Player 1" if self.one_score > self.two_score else "Player 2"
        self.write(f"Game Over! Winner is {winner}", move = False, align = "center", font = ("Helvetica", 24, "normal"))