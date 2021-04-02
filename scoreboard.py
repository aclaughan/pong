from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

        self.update(0,0)

    def update(self, l_point, r_point):
        self.l_score += l_point
        self.r_score += r_point
        self.goto(-50, 200)
        self.clear()
        self.write(
                self.l_score,
                align = "right",
                font = (
                        "Courier",
                        80,
                        "normal")
                )

        self.goto(50, 200)
        self.write(
                self.r_score,
                align = "left",
                font = (
                        "Courier",
                        80,
                        "normal")
                )

