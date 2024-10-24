from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.color(choice(COLORS))
        self.penup()
        self.goto(x=randint(-300, 600), y=randint(-240, 240))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.ht()

    def move(self,level):
        self.bk(STARTING_MOVE_DISTANCE + (level*MOVE_INCREMENT))

    def infinite_loop(self):
        if self.xcor()<-300:
            self.goto(x=300,y=self.ycor())



class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.generate_cars()
    def generate_cars(self):
        for i in range(20):
            self.cars.append(Car())



