from random import *
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        x_position = randint(-280, 280)
        y_position = randint(-280, 280)
        self.position = (x_position, y_position)
        self.goto(self.position)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")

    def generate_food(self):
        x_position = randint(-280, 280)
        y_position = randint(-280, 280)
        self.position = (x_position, y_position)
        self.goto(self.position)

    def detect_collision_with_food(self, head_position):
        """Detects if the heads x and y coordinate are within 15 pixels of each other"""
        if self.distance(head_position) < 15:  # 15 is an arbitrary distance threshold
            self.generate_food()  # Generate new food after eating
            return True
        return False