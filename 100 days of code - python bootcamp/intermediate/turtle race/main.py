from turtle import Turtle, Screen
import random

is_race_on = False
is_finished = False
screen = Screen()
screen.setup(width=1500, height=400)
user_bet = screen.textinput(title='make your bet', prompt='which turtle will win the race? Enter a color: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

tim = Turtle(shape='turtle')
tom = Turtle(shape='turtle')
jim = Turtle(shape='turtle')
jon = Turtle(shape='turtle')
ben = Turtle(shape='turtle')
dan = Turtle(shape='turtle')
turtles = [tim, tom, jim, jon, ben, dan]

def draw_finish_line(my_turtles: list[Turtle]):
    drawing_turtle = my_turtles[0]
    drawing_turtle.penup()
    drawing_turtle.goto(700, -200)
    drawing_turtle.setheading(90)
    drawing_turtle.pendown()
    drawing_turtle.pensize(5)
    while drawing_turtle.ycor() < 200:
        drawing_turtle.pencolor('red')
        drawing_turtle.forward(20)
        drawing_turtle.pencolor('blue')
        drawing_turtle.forward(20)
    drawing_turtle.pensize(1)
    drawing_turtle.setheading(0)

def set_color(turtle: Turtle, color: str):
    turtle.color(color)

def set_start_pos(turtle: Turtle, y_coord: int):
    turtle.penup()
    x_coord = -700
    turtle.goto(x_coord, y_coord)
    turtle.pendown()

def is_race_finished(is_finished):
    for turtle in turtles:
        if turtle.xcor() > 700:
            winning_color = turtle.pencolor()
            print(f'{winning_color} wins!')
            print('you won!') if winning_color == user_bet else print('you lose...')
            is_finished = True
            return is_finished
        
def move_turtles(turtle: Turtle):
    rand_distance = random.randint(0,10)
    turtle.forward(rand_distance)

draw_finish_line(turtles)

y = -150
for i in range(0, len(turtles)):
    set_color(turtles[i], colors[i])
    set_start_pos(turtles[i], y)
    y += 50

if user_bet:
    is_race_on = True

while is_race_on and not is_race_finished(is_finished= is_finished):

    for turtle in turtles:
        move_turtles(turtle)

screen.exitonclick()