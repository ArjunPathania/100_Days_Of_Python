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
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    screen.listen()
    screen.onkey(fun=player.move,key = "Up")
    for i in range(20):
        cars.cars[i].showturtle()
        cars.cars[i].move(scoreboard.score-1)
        if player.cross_finish_line():
            scoreboard.update_score()
            player.goto(x=0,y=-280)
        if player.detect_collision_with_car(cars.cars[i]):
            scoreboard.display_game_over()
            game_is_on = False
        cars.cars[i].infinite_loop()

screen.exitonclick()