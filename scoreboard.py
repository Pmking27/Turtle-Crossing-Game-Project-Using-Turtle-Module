from re import T
from tkinter import LEFT
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.update_scorebroad()
        

    def update_scorebroad(self):
        self.clear()
        self.write(f"Level {self.level}",align="left",font=FONT)
    
    def increase_level(self):
        self.level += 1
        self.update_scorebroad()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.",align="center",font=FONT)
        