from turtle import Turtle

FONT = ("Courier", 40, "bold")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 220)
        self.write(f"{self.l_score}", align="left", font=FONT)
        self.goto(100, 220)
        self.write(f"{self.r_score}", align="right", font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

