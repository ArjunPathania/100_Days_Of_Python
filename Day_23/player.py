from turtle import Turtle

# Constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move(self):
        """Move the player forward by MOVE_DISTANCE."""
        self.forward(MOVE_DISTANCE)

    def cross_finish_line(self):
        """Return True if the player reaches the finish line."""
        return self.ycor() > FINISH_LINE_Y

    def detect_collision_with_car(self, car):
        """Return True if the player collides with a car."""
        return self.distance(car) < 23

    def reset_position(self):
        """Reset the player's position to the starting point."""
        self.goto(STARTING_POSITION)
