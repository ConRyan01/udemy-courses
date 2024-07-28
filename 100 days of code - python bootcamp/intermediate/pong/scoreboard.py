from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, side: str):
        super().__init__()
        self.side = side
        self.score = 0
        self.hideturtle()
        self.set_position()
        self.color('white')
        self.write_score()

    def set_position(self):
        x_cord = 100 if self.side == 'right' else -100
        self.goto(x_cord, 240)

    def increase_score(self):
        self.score += 1
    
    def write_score(self):
        self.clear()
        self.write(self.score, align='center', font=("Arial", 30, "normal"))