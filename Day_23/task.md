
---
# Turtle Crossing Game

## Project Overview
The Turtle Crossing game is a simple arcade-style game built using Python's Turtle graphics library. The player controls a turtle that attempts to cross a busy road filled with cars moving from right to left. Each time the turtle successfully crosses the road, the player advances to the next level, where cars move faster, increasing the game's difficulty. If the turtle collides with a car, the game ends.

## Requirements
1. **Python 3.x**
2. **Turtle Graphics Library** (standard library in Python, no installation required)

## Game Features
- **Player Movement:** The player can control the turtle with the "Up" arrow key to move forward.
- **Car Manager:** Randomly generates cars of various colors that move horizontally across the screen.
- **Level Progression:** After crossing the road successfully, the level increases, and the cars move faster.
- **Scoreboard:** Displays the current level at the top of the screen. Displays "Game Over" message if the player collides with a car.
  
## Files

### `main.py`
- Sets up the screen and initializes the player, car manager, and scoreboard.
- Main game loop where:
  - The screen updates and listens for user input.
  - Each car moves across the screen, and collision checks are performed.
  - The player advances levels after crossing the finish line.
  - The game ends if the player collides with any car.

### `car_manager.py`
- Contains classes and methods related to the cars.
- **Classes:**
  - `Car`: Manages each individual car, including appearance, movement, and reset logic.
  - `CarManager`: Manages a list of `Car` objects, generating them at random positions.
  
### `player.py`
- Contains the `Player` class to control the turtle's movement and check if the player has crossed the road.
- **Key Methods:**
  - `move()`: Moves the player forward.
  - `cross_finish_line()`: Checks if the player has reached the finish line.
  - `detect_collision_with_car(car)`: Checks if the player has collided with a car.

### `scoreboard.py`
- Contains the `Scoreboard` class, which manages the game score (level) and displays "Game Over" upon collision.
- **Key Methods:**
  - `display_level()`: Displays the current level on the screen.
  - `increment_level()`: Increments the level and updates the display.
  - `display_game_over()`: Displays the "Game Over" message.

## Gameplay Instructions
1. Run the `main.py` file to start the game.
2. Use the "Up" arrow key to move the turtle forward.
3. Avoid the cars and try to reach the top of the screen.
4. Each successful crossing increases the level, making the cars move faster.
5. The game ends if the turtle collides with a car.

## Project Structure
```
turtle_crossing_game/
├── main.py           # Main game file, runs the game loop
├── car_manager.py    # Manages car objects and their movements
├── player.py         # Manages player movement and finish line detection
└── scoreboard.py     # Displays the current level and game over message
```

## Future Enhancements
Consider adding:
- Different car speeds for each car.
- Additional lanes with varying car directions.
- Special effects or sound upon level progression or collision.

## Authors
- **Arjun Pathania** - [GitHub](https://github.com/ArjunPathania/100_Days_Of_Python)
- 
---
