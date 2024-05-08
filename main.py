from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
ball = Ball()
pd = Paddle()
score = Score()
game_is_on = True
speed = ball.move_speed

screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(800, 600)
screen.tracer(0)

screen.listen()
screen.onkeypress(pd.fwd_r, 'Up')
screen.onkeypress(pd.bwd_r, 'Down')
screen.onkeypress(pd.fwd_l, 'w')
screen.onkeypress(pd.bwd_l, 's')

while game_is_on:
    screen.update()
    time.sleep(speed)
    ball.play()

    if 350 < ball.xcor() <= 370:
        if ball.distance(pd.pad_list[1]) <= 50:
            if ball.heading() == 45:
                ball.setheading(135)

            elif ball.heading() == 315:
                ball.setheading(225)

            speed *= 0.9

        else:
            score.l_score()
            ball.reset_position(ball.heading())
            speed = ball.move_speed

    elif -350 > ball.xcor() >= -370:
        if ball.distance(pd.pad_list[0]) <= 50:
            if ball.heading() == 135:
                ball.setheading(45)

            elif ball.heading() == 225:
                ball.setheading(315)

            speed *= 0.9

        else:
            score.r_score()
            ball.reset_position(ball.heading())
            speed = ball.move_speed

screen.exitonclick()
