from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, side: str = 'right'):
        super().__init__()
        self.side = side
        self.create_paddle()

    def create_paddle(self):
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        if self.side == 'right':
            self.goto(350, 0)
        else:
            self.goto(-350, 0)

    def move(self, direction: str):
        new_y = self.ycor() + 20 if direction == 'up' else self.ycor() - 20
        self.goto(self.xcor(), new_y)

