from turtle import Screen #,Turtle

# def draw_middle_line():
#     """Draw a dashed line in the middle of the screen."""
#     line_turtle = Turtle()
#     line_turtle.hideturtle()
#     line_turtle.color("white")
#     line_turtle.penup()
#     line_turtle.goto(0, 300)  # Start drawing from the top of the screen
#     line_turtle.setheading(270)  # Point the turtle downward
#     line_turtle.width(5)
#
#     # Draw dashed line
#     for i in range(30):  # Change to 15 for better visibility
#         line_turtle.pendown()
#         line_turtle.forward(10)
#         line_turtle.penup()
#         line_turtle.forward(10)


class GameScreen:
    def __init__(self):
        """Initialize the game screen with title, dimensions, and background color."""
        self.screen = Screen()
        self.setup_screen()
        # draw_middle_line()

    def setup_screen(self):
        """Set up the main game screen properties."""
        self.screen.setup(width=800, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Pong")
        self.screen.tracer(0)  # Disable auto screen updates for smoother animations


if __name__ == "__main__":
    game_screen = GameScreen()
    game_screen.screen.mainloop()  # Keep the window open
