from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=position[0], y=position[1])
        self.score = 0
        self.update_score()

    def update_score(self):
        """
        Update and display the current score.
        """
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increment_score(self):
        """
        Increment the score, clear the previous score, and update the display.
        """
        self.score += 1
        self.clear()
        self.update_score()

