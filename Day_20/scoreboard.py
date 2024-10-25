from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.playerScore = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.ht()

        # Load high score, handling possible issues with file contents
        try:
            with open("high_score.txt", mode='r') as file:
                self.highScore = int(file.read().strip() or 0)  # Default to 0 if empty
        except (FileNotFoundError, ValueError):
            self.highScore = 0

        self.display_score()

    def display_score(self):
        """Display the current score and high score."""
        self.clear()
        self.write(arg=f"Score: {self.playerScore} High Score: {self.highScore}",
                   move=False, align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        """Increment the score and update the display."""
        self.playerScore += 1
        self.display_score()

    def update_high_score(self):
        """Update high score if current score is higher, and save to file."""
        if self.playerScore > self.highScore:
            self.highScore = self.playerScore  # Update the high score
            with open("high_score.txt", mode='w') as file:
                file.write(str(self.highScore))  # Write the new high score to the file
        self.display_score()  # Refresh display with updated high score
