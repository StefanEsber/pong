from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score

# Main screen of game, pixels used in functions
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-370, 0))
r_paddle = Paddle((370, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
game_is_on = True
while game_is_on:
    screen.update()
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if ball.distance(l_paddle) < 50 and ball.xcor() < - 370 or ball.distance(r_paddle) < 50 and ball.xcor() > 370:
        ball.bounce_paddle()

    if ball.xcor() > 390:
        score.increase_l_score()
        ball.refresh()
    if ball.xcor() < - 390:
        score.increase_r_score()
        ball.refresh()
screen.exitonclick()
