from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.draw_grass()
        self.draw_road()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.write(font=FONT, arg=f'Level: {self.level}')

    def draw_grass(self):
        self.pencolor('green')
        self.penup()
        self.goto(300, -290)
        self.pensize(40)
        self.pendown()
        self.goto(-300, -290)
        self.penup()
        self.goto(300, 290)
        self.pendown()
        self.goto(-300, 290)
        self.pencolor('black')

    def draw_road(self):
        self.pencolor('white')
        self.pensize(3)
        for lane in range(-250, 275, 25):
            self.penup()
            self.goto(300, lane)
            self.setheading(180)
            while self.xcor() > -330:
                self.pendown()
                self.forward(30)
                self.penup()
                self.forward(30)
        self.pencolor('black')

    def game_over(self):
        self.home()
        self.write(font=FONT, align='center', arg='GAME OVER')

    def level_up(self):
        self.level += 1
        self.goto(-280, 260)
        self.write(f'Level: {self.level}', font=FONT)
