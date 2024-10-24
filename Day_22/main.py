from screen import GameScreen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

def setup_game():
    """Sets up the game components (screen, paddles, ball, scoreboards)."""
    screen = GameScreen()
    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0))
    ball = Ball()
    l_scoreboard = ScoreBoard((-40, 250))
    r_scoreboard = ScoreBoard((40, 250))
    return screen, l_paddle, r_paddle, ball, l_scoreboard, r_scoreboard

def check_score(l_scoreboard, r_scoreboard, screen,game_length):
    """Checks if either player has won and asks if they want to play again."""
    if l_scoreboard.score >= game_length or r_scoreboard.score >= game_length:
        winner = "Player One" if l_scoreboard.score >= game_length else "Player Two"
        return screen.screen.textinput(title="Game Over", prompt=f"{winner} Won! Play Again? 'y' or 'n' :").lower()
    return None

def game_loop(screen, l_paddle, r_paddle, ball, l_scoreboard, r_scoreboard):
    """Runs the main game loop."""
    is_game_on = True
    game_length = int(screen.screen.textinput(title="Game Length",prompt="Enter game length: (5/10/15) points "))
    time.sleep(3) # give time player to get ready
    while is_game_on:
        screen.screen.update()
        screen.screen.listen()
        screen.screen.onkey(fun=r_paddle.up, key='Up')
        screen.screen.onkey(fun=r_paddle.down, key='Down')
        screen.screen.onkey(fun=l_paddle.up, key='w')
        screen.screen.onkey(fun=l_paddle.down, key='s')

        time.sleep(ball.move_speed)
        ball.move_ball()
        ball.detect_collision_with_wall()
        ball.detect_collision_with_paddle(l_paddle)
        ball.detect_collision_with_paddle(r_paddle)
        ball.ball_out_of_bounds()


        if ball.xcor() > 390:
            l_scoreboard.update_score()
        elif ball.xcor() < -390:
            r_scoreboard.update_score()

        play_again = check_score(l_scoreboard, r_scoreboard, screen,game_length)
        if play_again == 'n':
            is_game_on = False
        elif play_again == 'y':
            screen.screen.reset()
            screen, l_paddle, r_paddle, ball, l_scoreboard, r_scoreboard = setup_game()

    screen.screen.exitonclick()

def main():
    screen, l_paddle, r_paddle, ball, l_scoreboard, r_scoreboard = setup_game()
    game_loop(screen, l_paddle, r_paddle, ball, l_scoreboard, r_scoreboard)


if __name__ == "__main__":
    main()
