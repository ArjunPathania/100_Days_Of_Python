import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

# Initialize game components
player = Player()
cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Player controls
    screen.listen()
    screen.onkey(fun=player.move, key="Up")

    # Move each car and check for collisions
    for car in cars.cars:
        car.showturtle()
        car.move(scoreboard.level - 1)

        # Check if player crossed the finish line
        if player.cross_finish_line():
            scoreboard.increment_level()
            player.reset_position()

        # Check for collision with car
        if player.detect_collision_with_car(car):
            scoreboard.display_game_over()
            game_is_on = False

        car.reset_if_out_of_bounds()

screen.exitonclick()
