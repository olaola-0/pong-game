# Paddle Ball Game

This repository hosts the source code for an Paddle Ball Game, a contemporary rendition of the timeless Pong game, implemented in Python with the use of the `turtle` module for rendering. The game features enhanced object-oriented programming practices to ensure code modularity, readability, and maintainability.

## Overview

The game is constructed with Python, leveraging the Turtle Graphics Library for its graphical output. It includes a two-player mode where players control paddles to hit a ball back and forth across the screen. The objective is to surpass the opponent by achieving a higher score, which is incremented each time an opponent fails to return the ball.

## Repository Structure

- `ball.py`: Defines the `Ball` class, controlling the ball's movement, collision detection, and interaction with game boundaries and paddles.
- `main.py`: The entry point of the game, setting up the game window, initializing game components, and managing the game loop.
- `paddle.py`: Contains the `Paddle` class for creating and managing paddle objects, including their movement and positioning.
- `scoreboard.py`: Implements the `Scoreboard` class for displaying and updating the game score.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system. The game uses the built-in `turtle` graphics library, so no additional installations are required.

### Running the Game

Clone the repository to your local machine and navigate to the project directory. Run the game using Python:

```bash
python main.py
