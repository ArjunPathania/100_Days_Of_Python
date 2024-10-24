from turtle import Turtle

# Constants
FONT = ("Courier", 24, "normal")
LEVEL_POSITION = (-230, 250)
GAME_OVER_POSITION = (0, 0)
GAME_OVER_FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.ht()  # Hide the turtle icon
        self.goto(LEVEL_POSITION)
        self.display_level()

    def display_level(self):
        """Displays the current level on the screen."""
        self.clear()
        self.write(f"LEVEL: {self.level}", align="center", font=FONT)

    def increment_level(self):
        """Increments the level and updates the display."""
        self.level += 1
        self.display_level()

    def display_game_over(self):
        """Display a Game Over message in the center of the screen."""
        self.goto(GAME_OVER_POSITION)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
