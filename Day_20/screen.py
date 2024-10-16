from turtle import Screen

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.title("My Snake Game")
        self.screen.bgcolor("black")
        self.screen.tracer(0)  # Disable auto screen updates
