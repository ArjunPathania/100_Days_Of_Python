from scoreboard import ScoreBoard
from snake import SnakeBody
from screen import GameScreen
from food import Food
import time

game_screen = GameScreen()
snake_body = SnakeBody()
food = Food()
score = ScoreBoard()
# game_screen.screen.update()  # Update the screen after every movement

is_game_on = True
while is_game_on:
    player_score = 0
    game_screen.screen.listen()
    time.sleep(0.1)  # Add a delay so the snake doesn't move too fast
    snake_body.move()
    game_screen.screen.update()  # Update the screen after every movement
    game_screen.screen.onkey(fun=snake_body.up, key="Up")
    game_screen.screen.onkey(fun=snake_body.down, key="Down")
    game_screen.screen.onkey(fun = snake_body.left,key = "Left")
    game_screen.screen.onkey(fun = snake_body.right,key = "Right")
    if food.detect_collision_with_food(snake_body.head):
        snake_body.extend()
        score.update_score()
    if snake_body.detect_collision_with_wall() or snake_body.detect_collision_with_self():
        user_response= game_screen.screen.textinput(title=f"Game Over",prompt="Play Again? 'Y' or 'N'").lower()
        if user_response == 'y':
            game_screen.screen.reset()
            game_screen = GameScreen()
            snake_body = SnakeBody()
            food = Food()
            score = ScoreBoard()
            continue
        else:
            is_game_on = False

game_screen.screen.mainloop()
