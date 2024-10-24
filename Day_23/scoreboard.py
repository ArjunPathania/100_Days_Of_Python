from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()  # Prevent drawing when moving the turtle
        self.ht()  # Hide the turtle as we don't need to see the turtle icon
        self.goto(x=-230,y=250)
        self.display_score()

    def display_score(self):
        """Displays the current score on the screen."""
        self.clear()  # Clear the previous score before writing the new one
        self.write(f"LEVEL: {self.score}", align="center", font=("Courier", 20, "normal"))

    def update_score(self):
        """Updates the score by incrementing it and displaying the new score."""
        self.score += 1
        self.display_score()

    def display_game_over(self):
        self.goto(x=0,y=0)
        self.write(f"GAME OVER", align="center", font=("Courier", 80, "normal"))


