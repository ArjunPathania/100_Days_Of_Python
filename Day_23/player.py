from  turtle import Turtle
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
        self.fd(MOVE_DISTANCE)

    def cross_finish_line(self):
        if self.ycor()>FINISH_LINE_Y:
            return True

    def detect_collision_with_car(self,car):
        if self.distance(car)<23 and (-280 < self.ycor() < 280):
            return True

