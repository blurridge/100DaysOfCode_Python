# Scoreboard

from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("high_score.txt", mode="r") as file:
            high_score = int(file.read())
        self.score = 0
        self.high_score = high_score
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 240)
        self.write_scoreboard()
    
    def write_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", move = False, align = "center", font = ("Helvetica", 24, "normal"))
    
    def reset_scoreboard(self):
        self.clear()
        self.high_score = self.score if self.score > self.high_score else self.high_score
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.score = 0
        self.write_scoreboard()