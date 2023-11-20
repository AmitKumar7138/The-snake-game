# Snake Game Project

## Introduction
This project is a Python-based implementation of the classic Snake Game. It uses the `turtle` module for graphics and event handling. The game features a snake that the player controls, aiming to eat food that randomly appears on the screen. Each time the food is consumed, the snake grows, and the player earns points.

## File Descriptions
1. **food.py**
   - **Purpose**: Defines the `Food` class, a subclass of the Turtle class. This class is responsible for displaying food on the game screen and randomly changing its position.
   - **Key Features**: Random placement of food, graphical representation as a blue dot.

2. **main.py**
   - **Purpose**: The main script to run the snake game. It sets up the game window, initializes game objects like the snake, food, and scoreboard, and contains the game loop.
   - **Key Features**: Game initialization, event handling for keyboard inputs, main game loop.

3. **scoreboard.py**
   - **Purpose**: Defines the `ScoreBoard` class for displaying and updating the game score. Inherits from the Turtle class.
   - **Key Features**: Score display at the top of the game screen, score updating mechanism.

4. **snake.py**
   - **Purpose**: Contains the `Snake` class, which manages the snake's behavior in the game, including its size, movement, and growth.
   - **Key Features**: Snake creation, movement control, snake growth upon eating food.

## Setup and Running the Game
1. **Prerequisites**: Ensure you have Python installed on your system. This game is developed using Python 3.x.

2. **Running the Game**:
   - Clone or download the project files to your local machine.
   - Navigate to the project directory in your terminal or command prompt.
   - Run the command `python main.py` to start the game.
   - Use the arrow keys to control the snake's movement.

## Gameplay
- The goal is to control the snake to eat the blue dots (food) that appear randomly on the screen.
- Each time the snake eats the food, it grows in length, and the score increases.
- The game ends if the snake runs into the screen border or into itself.

## Contributions
- This project is open for contributions and improvements. Feel free to fork the repository, make changes, and submit a pull request.

