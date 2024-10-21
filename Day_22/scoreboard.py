from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, coordinates):
        """Initialize the scoreboard at the given coordinates with a starting score of 0."""
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()  # Prevent drawing when moving the turtle
        self.ht()  # Hide the turtle as we don't need to see the turtle icon
        self.goto(coordinates)
        self.display_score()

    def display_score(self):
        """Displays the current score on the screen."""
        self.clear()  # Clear the previous score before writing the new one
        self.write(f"{self.score}", align="center", font=("Courier", 40, "normal"))

    def update_score(self):
        """Updates the score by incrementing it and displaying the new score."""
        self.score += 1
        self.display_score()
