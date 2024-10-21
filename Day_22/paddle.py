from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coordinates):
        """Initialize the paddle at the given coordinates."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(10)
        self.goto(coordinates)

    def up(self):
        """Move the paddle up by 20 units, but limit movement within the top boundary."""
        if self.ycor() < 220:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        """Move the paddle down by 20 units, but limit movement within the bottom boundary."""
        if self.ycor() > -220:
            self.goto(x=self.xcor(), y=self.ycor() - 20)
