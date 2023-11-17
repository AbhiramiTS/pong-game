from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=4)
        self.goto(x=x_cor, y=0)
        # self.speed(100)

    def up(self):
        y_cor = self.ycor()
        if y_cor < 200:
            self.goto(x=self.xcor(), y=y_cor + 20)

    def down(self):
        y_cor = self.ycor()
        if y_cor > -200:
            self.goto(x=self.xcor(), y=y_cor - 20)


