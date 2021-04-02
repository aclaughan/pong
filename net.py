from turtle import Turtle

class Net(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, y = 300)
        self.setheading(to_angle = 270)
        self.pensize(width = 5)
        self.color("white")
        self.pendown()
        for dash in range(22):
            self.forward(distance = 12)
            self.penup()
            self.forward(distance = 16)
            self.pendown()

