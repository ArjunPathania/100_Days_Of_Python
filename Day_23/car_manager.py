from turtle import Turtle
from random import choice, randint

# Constants
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
SCREEN_WIDTH = 600
CAR_LIMIT = 20

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=randint(-SCREEN_WIDTH // 2, SCREEN_WIDTH // 2), y=randint(-240, 240))
        self.ht()

    def move(self, level):
        """Move the car backward by the calculated distance."""
        self.backward(STARTING_MOVE_DISTANCE + (level * MOVE_INCREMENT))

    def reset_if_out_of_bounds(self):
        """Reset car position when it moves out of bounds."""
        if self.xcor() < -SCREEN_WIDTH // 2:
            self.goto(x=SCREEN_WIDTH // 2, y=self.ycor())


class CarManager:
    def __init__(self):
        self.cars = []
        self.generate_cars()

    def generate_cars(self):
        """Generate a list of cars at random positions."""
        for _ in range(CAR_LIMIT):
            self.cars.append(Car())
