from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 0.12
        self.y_move = 0.12
        self.speed = 0

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def bounce_paddle(self):
        self.x_move *= -(1+self.speed)
        self.speed += 0.15

    def refresh(self):
        self.speed = 0
        self.x_move = 0.12
        self.clear()
        self.home()
