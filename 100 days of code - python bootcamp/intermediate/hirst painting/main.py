import colorgram
import turtle
import random

# rgb_colors = []
# colors = colorgram.extract('C:\\Users\\ryanc\\Documents\\github\\Python-3\\Udemy Courses\\100 days of code - python bootcamp\\intermediate\\hirst painting\\image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_tup = (r, g, b)
#     rgb_colors.append(new_tup)

rgb_colors = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), 
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), 
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), 
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), 
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

my_turtle = turtle.Turtle()
turtle.Screen().colormode(255)
my_turtle.shape('arrow')
my_turtle.penup()
my_turtle.speed('fastest')

def draw_dot_line(y_pos):
    for x_pos in range(-5, 5):
        my_turtle.setpos(x_pos * 50, y_pos)
        my_turtle.dot(20, random.choice(rgb_colors))

for i in range(-5, 5):
    draw_dot_line(i * 50)

turtle.exitonclick()
