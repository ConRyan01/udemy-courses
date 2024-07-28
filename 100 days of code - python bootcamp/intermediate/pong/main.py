from time import sleep
from turtle import Screen

from play_field import PlayField 
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

field = PlayField()
paddle_r = Paddle()
paddle_l = Paddle(side='left')
ball = Ball()
score_r = Scoreboard(side = 'right')
score_l = Scoreboard(side = 'left')
screen.update()
game_is_on = True
winner = None

screen.listen()
screen.onkeypress(lambda: paddle_r.move(direction='up'), 'Up')
screen.onkeypress(lambda: paddle_r.move(direction='down'), 'Down')
screen.onkeypress(lambda: paddle_l.move(direction='up'), 'w')
screen.onkeypress(lambda: paddle_l.move(direction='down'), 's')

while game_is_on:
    screen.update()
    ball.move()
    if not ball.bounce(paddle_r=paddle_r, paddle_l=paddle_l):
        if ball.xcor() <= -400:
            score_r.increase_score()
            score_r.write_score()
        elif ball.xcor() >= 400:
            score_l.increase_score()
            score_l.write_score()
        ball.reset_position()

    if score_l.score == 10:
        winner = 'Left'
        break
    elif score_r.score == 10:
        winner = 'Right'
        break
    
    sleep(0.01)

field.color('white')
field.write(f'Game Over! {winner} player wins!', align='center', font=('Arial', 40, 'normal'))
screen.update()


screen.exitonclick()