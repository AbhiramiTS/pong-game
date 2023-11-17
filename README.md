# The Pong Game 🎮

Welcome to "The Pong Game" – a classic arcade game implemented in Python using the Turtle graphics library.

## Project Overview 🚀

This project aims to recreate the classic Pong game, allowing users to play against each other with paddles and a bouncing ball. The game features two paddles, one on each side of the screen, and a ball that moves between them. The objective is to bounce the ball past the opponent's paddle to score points.

## Project Structure 📂

The project is organized into multiple Python files for better code organization:

- `main.py`: The main script that initializes the game and manages the game loop.
- `paddle.py`: Contains the Paddle class responsible for creating and controlling the paddles.
- `ball.py`: Defines the Ball class, handling the ball's movement and interactions.
- `scoreboard.py`: Manages the scoring system and displays the current score on the screen.

## How to Play 🎯

- Use the **Up** and **Down** arrow keys for the right paddle.
- Use the **W** and **S** keys for the left paddle.

## Known Issues 🚧

**Project Status: Incomplete**

The project is currently under development, and the following issues are yet to be resolved:

1. **Scoring Issue**: When the ball hits the paddle, only the left score (`l_score`) updates, and the right score (`r_score`) remains unchanged.

2. **Bouncing Range Issue**: Occasionally, the ball may bounce within a small range after hitting a paddle before changing direction, causing unexpected behavior.

## Contributions 🤝

Contributions and suggestions are welcome! Feel free to submit issues or pull requests to help improve the game.

## Screenshots 📷

![Gameplay Screenshot](screenshots/gameplay.png)
