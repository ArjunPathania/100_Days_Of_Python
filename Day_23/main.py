import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
player = Player()
cars = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(fun=player.move,key = "Up")
    for i in range(50):
        cars.cars[i].showturtle()
        cars.cars[i].move()
        if player.cross_finish_line() or player.detect_collision_with_car(cars.cars[i]):
            game_is_on = False

