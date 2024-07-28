from turtle import Turtle

LINE_START_COORDS = (0, -300)
SCREEN_HEIGHT = 600

class PlayField(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.create_center_line()
        
    def create_center_line(self):
        line = Turtle()
        line.hideturtle()
        line.speed('fastest')
        line.color('white')
        line.shape('square')
        line.pensize(5)
        line.penup()
        line.goto(LINE_START_COORDS)
        self.draw_line(line)
        self.goto(0, 100)
    
    def draw_line(self, turtle: Turtle, dotted: bool = True, segment_length: int = 40):
        height = SCREEN_HEIGHT
        while height > 0:
            if dotted:
                turtle.pendown()
                turtle.setheading(90)
                turtle.forward(segment_length)
                turtle.penup()
                turtle.forward(segment_length)
                height -= segment_length*2
            else:
                turtle.pendown()
                turtle.setheading(90)
                turtle.forward(height)
                height = 0
