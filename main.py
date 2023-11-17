import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# Set up the game screen
screen = Screen()
screen.setup(height=500, width=800)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)  # Turn off automatic screen updates

# Define positions for the score displays
LEFT_SCORE_POSITION = (-220, 200)
RIGHT_SCORE_POSITION = (220, 200)

# Create paddles, ball, and scoreboards
r_paddle = Paddle(360)
l_paddle = Paddle(-360)
ball = Ball()
r_score = Scoreboard(RIGHT_SCORE_POSITION)
l_score = Scoreboard(LEFT_SCORE_POSITION)

# Listen for key events to control paddles
screen.listen()
screen.onkey(key="Down", fun=r_paddle.down)
screen.onkey(key="Up", fun=r_paddle.up)
screen.onkey(key="w", fun=l_paddle.up)
screen.onkey(key="s", fun=l_paddle.down)

# Game loop
game_on = True
while game_on:
    screen.update()  # Update the screen manually
    time.sleep(0.1)  # Introduce a small delay for smoother gameplay
    ball.move()

    print(ball.xcor())
    # Detect collision with right and left paddle
    if ball.distance(r_paddle) < 50:
        print(ball.xcor())  # Print ball's x-coordinate for debugging
        if ball.xcor() <= -300:
            l_score.increment_score()
        if ball.xcor() >= 320:
            print("ball.xcor():", ball.xcor())  # Print ball's x-coordinate for debugging
            r_score.increment_score()
        ball.x_bounce()
        # ball.move_speed *= 0.9  # Possible speed adjustment

    # Detect collision with wall (y-axis)
    if ball.ycor() > 220 or ball.ycor() < -220:
        ball.y_bounce()

    # Ball misses the right wall
    if ball.xcor() > 360:
        ball.reset_position()
        l_score.increment_score()

    # Ball misses the left wall
    if ball.xcor() < -360:
        ball.reset_position()
        r_score.increment_score()

# Close the game window when clicked
screen.exitonclick()
