from snake import SnakeBody
from screen import GameScreen
import time

game_screen = GameScreen()
snake_body = SnakeBody()

# game_screen.screen.update()  # Update the screen after every movement

is_game_on = True
while is_game_on:
    game_screen.screen.listen()
    time.sleep(0.1)  # Add a delay so the snake doesn't move too fast
    snake_body.move()
    game_screen.screen.update()  # Update the screen after every movement
    game_screen.screen.onkey(fun=snake_body.up, key="Up")
    game_screen.screen.onkey(fun=snake_body.down, key="Down")
    game_screen.screen.onkey(fun = snake_body.left,key = "Left")
    game_screen.screen.onkey(fun = snake_body.right,key = "Right")



game_screen.screen.mainloop()
