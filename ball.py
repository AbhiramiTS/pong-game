from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1

    def move(self):
        y = self.ycor() + self.y_cor
        x = self.xcor() + self.x_cor
        self.goto(x=x, y=y)

    def y_bounce(self):
        self.y_cor *= -1

    def x_bounce(self):
        self.x_cor *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.x_bounce()
