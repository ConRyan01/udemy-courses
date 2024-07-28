from turtle import Turtle
from time import sleep
import os

HIGH_SCORE_PATH = 'C:\\Users\\mwysz\\OneDrive\\Documents\\Github\\Python-3\\Udemy Courses\\100 days of code - python bootcamp\\intermediate\\snake game'
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        if not os.path.exists(f'{HIGH_SCORE_PATH}\\high_score.txt' ):
            with open(f'{HIGH_SCORE_PATH}\\high_score.txt', mode='w') as file:
                file.write('0')
        with open(f'{HIGH_SCORE_PATH}\\high_score.txt', mode='r') as file:
            self.high_score = file.read()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High Score: {self.high_score}', align = ALIGNMENT, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = str(self.score)
            with open(f'{HIGH_SCORE_PATH}\\high_score.txt', mode= 'w') as file:
                file.write(self.high_score)
        self.score = 0
        self.update_scoreboard()

    def set_speed(self):
        speed = 0.1
        if self.score > 9 and self.score < 20:
            speed = 0.08
        elif self.score > 19 and self.score < 30:
            speed = 0.05
        elif self.score > 29 and self.score < 40:
            speed = 0.03
        elif self.score > 39:
            speed = 0.01

        return sleep(speed)
            

        
