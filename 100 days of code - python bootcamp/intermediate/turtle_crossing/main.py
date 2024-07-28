import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('grey')

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkeypress(player.move, 'Up')

game_is_on = True
while game_is_on:
    car_manager.random_car_generator()
    car_manager.move_cars()
    car_manager.remove_offscreen_cars()
    if car_manager.detect_squish(player):
        scoreboard.game_over()
        game_is_on = False
    if player.ycor() >= 280:
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.clear()
        scoreboard.draw_grass()
        scoreboard.draw_road()
        scoreboard.level_up()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
