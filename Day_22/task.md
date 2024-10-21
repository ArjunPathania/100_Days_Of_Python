Here's the updated `task.md` file that includes information about how the ball's movement was changed and how the edge of the paddle was detected.

### Updated task.md
```markdown
# Pong Game Development Tasks

## 1. Pong Game Development
### Problem Statement
Create a functional Pong game where two players can control paddles to hit a ball back and forth. The game should track scores, implement collision detection, and allow players to restart the game after a win.

### Initial Features
- Two paddles controlled by players.
- A ball that moves and bounces off the paddles and walls.
- A scoreboard to keep track of scores.

### Improvements
- Added game reset functionality when a player reaches a score of 5.
- Enhanced collision detection between the ball and paddles for better gameplay.
- Improved user interface by clearly displaying scores and providing restart options.

---

## 2. Error Handling in the Scoreboard
### Problem Statement
While running the game, an error was encountered regarding the scoreboard's `write` method, causing the game to crash.

### Initial Code
```python
self.write(f"{self.score}", True, align=align, font=("Arial", 12, "normal"))
```

### Improvements
- The method `write` was called without ensuring the parameters were correctly formatted.
- The score display functionality was streamlined by creating a `display_score()` helper method to avoid repetition.

### Refactored Code
```python
def display_score(self):
    """Displays the current score on the screen."""
    self.clear()  # Clear the previous score before writing the new one
    self.write(f"{self.score}", align="center", font=("Courier", 40, "normal"))
```

---

## 3. Game Reset Functionality
### Problem Statement
The game did not restart after a player won; instead, it only ended without giving players an option to play again.

### Initial Code
```python
if l_scoreboard.score>=5 or r_scoreboard.score>=5:
    play_again = screen.screen.textinput(title="Game Over", prompt="Play Again? 'y' or 'n' :").lower()
    if play_again == 'n':
        is_game_on = False
```

### Improvements
- The game logic was improved to allow for a reset when the user enters 'y'.
- Added code to reset paddles, the ball, and the scoreboard upon restarting.

### Refactored Code
```python
if play_again == 'y':
    screen.screen.reset()
    # Reset the game elements
```

---

## 4. Paddle Movement Constraints
### Problem Statement
The paddles were not allowed to move beyond a certain boundary, but the logic was unclear and contained unnecessary checks.

### Initial Code
```python
if self.ycor() > 220:
    pass
```

### Improvements
- The conditions in the `up()` and `down()` methods were simplified to ensure clearer logic without using `pass`.
- Improved readability and maintainability.

### Refactored Code
```python
def up(self):
    """Move the paddle up by 20 units, but limit movement within the top boundary."""
    if self.ycor() < 220:
        self.goto(x=self.xcor(), y=self.ycor() + 20)
```

---

## 5. Ball Movement and Collision Detection
### Problem Statement
Initially, the ball's movement was implemented using the Turtle's `fd` method, making it difficult to control its direction independently.

### Initial Code
```python
self.fd(10)
```

### Improvements
- The movement of the ball was modified to use independent x and y coordinates for more control.
- The ball's movement is now based on adjusting its x and y values separately, which allows for more precise handling of collisions.

### Refactored Code
```python
def move_ball(self):
    """Move the ball according to its current x and y coordinates."""
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)
```

### Edge of the Paddle Detection
- The ball detects collisions with the paddles by calculating the distance between itself and the paddle positions.
- The edge of the paddle is detected using conditions that check both the distance from the paddle and the ball's x-coordinate.

### Refactored Code for Paddle Collision Detection
```python
def detect_collision_with_paddle(self, paddle_position):
    if self.distance(paddle_position) < 50 and abs(self.xcor()) > 320:
        self.x_move *= -1  # Reverse the ball's x direction upon collision
```

---

## 6. Game Screen Setup
### Problem Statement
The `GameScreen` class setup was functional but could benefit from better structure and readability.

### Initial Code
```python
self.turtle.teleport(x=0,y=500)
```

### Improvements
- Modularized the setup into separate methods for screen setup and drawing the middle line.
- Improved the logic for drawing the dashed line in the center of the screen.

### Refactored Code
```python
def setup_screen(self):
    """Set up the main game screen properties."""
    self.screen.setup(width=800, height=600)
    self.screen.bgcolor("black")
    self.screen.title("Pong")
```

---

# Conclusion
These improvements enhance the overall readability, maintainability, and functionality of the Pong game code, ensuring a smoother gaming experience and clearer logic.
```
g