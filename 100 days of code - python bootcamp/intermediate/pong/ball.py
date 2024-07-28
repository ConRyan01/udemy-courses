from turtle import Turtle
import random, time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, random.randrange(-260, 260, 20))
        self.setheading(random.choice([1, 3, 5, 7]) * 45)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.03
        self.move()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        time.sleep(self.ball_speed)

    def bounce(self, paddle_r: Turtle, paddle_l: Turtle) -> bool:
        is_y_bounce = self.ycor() >= 280 or self.ycor() <= -280
        is_paddle_r_collision = self.xcor() >= 330 and self.distance(paddle_r) <= 50
        is_paddle_l_collision = self.xcor() <= -330 and self.distance(paddle_l) <= 50
        is_ball_out_of_bounds = self.xcor() >= 400 or self.xcor() <= -400

        if is_y_bounce:
            self.y_move *= -1

        if is_paddle_l_collision or is_paddle_r_collision:
            self.x_move *= -1
            self.ball_speed *= 0.9

        elif is_ball_out_of_bounds:
            return False

        return True

    def reset_position(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.ball_speed = 0.03

    