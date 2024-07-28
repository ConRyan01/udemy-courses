from turtle import Turtle
from typing import List

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        
        self.segments: List[Turtle] = []
        self.last_segment = None
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for pos in STARTING_POSITIONS:
            new_segment = Turtle()
            new_segment.shape('square')
            new_segment.color('white')
            new_segment.penup()
            new_segment.goto(pos)
            self.segments.append(new_segment)
            self.last_segment = self.segments[-1]

    def add_segment(self):
        new_segment = Turtle()
        new_segment.shape('square')
        new_segment.color('white')
        new_segment.penup()
        position_reference = self.last_segment.position()
        last_segment_dir = self.last_segment.heading()

        if last_segment_dir == 0:
            new_segment.setpos(position_reference[0] - 20, position_reference[1])
        elif last_segment_dir == 90:
            new_segment.setpos(position_reference[0], position_reference[1] - 20)
        elif last_segment_dir == 180:
            new_segment.setpos(position_reference[0] + 20, position_reference[1])
        else:
            new_segment.setpos(position_reference[0], position_reference[1] + 20)
        
        self.segments.append(new_segment)
        self.last_segment = new_segment

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.last_segment = None
        self.create_snake()
        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)