from scoreboard import ScoreBoard
from snake import SnakeBody
from screen import GameScreen
from food import Food
import time

game_screen = GameScreen()
snake_body = SnakeBody()
food = Food()
score = ScoreBoard()

is_game_on = True
while is_game_on:
    game_screen.screen.listen()
    time.sleep(0.1)  # Add a delay so the snake doesn't move too fast
    snake_body.move()
    game_screen.screen.update()  # Update the screen after every movement

    # Listen for direction changes
    game_screen.screen.onkey(fun=snake_body.up, key="Up")
    game_screen.screen.onkey(fun=snake_body.down, key="Down")
    game_screen.screen.onkey(fun=snake_body.left, key="Left")
    game_screen.screen.onkey(fun=snake_body.right, key="Right")

    # Check for food collision
    if food.detect_collision_with_food(snake_body.head):
        snake_body.extend()
        score.update_score()

    # Check for collisions with wall or itself
    if snake_body.detect_collision_with_wall() or snake_body.detect_collision_with_self():
        score.update_high_score()  # Update high score before restarting or exiting

        # Ask if the player wants to play again
        user_response = game_screen.screen.textinput(title="Game Over", prompt="Play Again? 'Y' or 'N'").lower()
        if user_response == 'y':
            # Reset game components for a new game
            game_screen.screen.reset()
            game_screen = GameScreen()
            snake_body = SnakeBody()
            food = Food()
            score = ScoreBoard()
            continue
        else:
            is_game_on = False

game_screen.screen.exitonclick()
