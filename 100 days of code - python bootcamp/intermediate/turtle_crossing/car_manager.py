from turtle import Turtle
import random
from typing import List

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.cars: List[Turtle] = []
        self.car_gen_chance = 5

    def generate_car(self):
        new_car = Turtle()
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(320, random.randrange(-250, 250, 10))
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_distance)

    def random_car_generator(self):
        if random.randint(1,self.car_gen_chance) == 1:
            self.generate_car()
    
    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
        if self.car_gen_chance > 1:
            self.car_gen_chance -= 1

    def detect_squish(self, turtle: Turtle) -> bool | None:
        for car in self.cars:
            if car.distance(turtle) < 20:
                return True
            
    def remove_offscreen_cars(self):
        for car in self.cars:
            if car.xcor() < -330:
                self.cars.remove(car)

