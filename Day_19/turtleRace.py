from turtle import Turtle, Screen
from random import randint

# Define a list of turtle colors
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

# Class to represent each Contestant (Turtle) in the race
class Contestant:
    def __init__(self, color, start_x, start_y):
        self.turtle = Turtle(shape="turtle")  # Create a turtle with turtle shape
        self.turtle.penup()                   # Lift the pen so the turtle doesn't draw lines
        self.turtle.color(color)              # Set the turtle's color
        self.turtle.goto(x=start_x, y=start_y) # Place the turtle at the starting position

# Class to manage the Race and its logic
class Race:
    def __init__(self):
        self.contestants = []  # A list to hold the turtle contestants
        start_x = -230         # X-coordinate for the starting position
        y_positions = [70, 40, 10, -20, -50, -80]  # Y-positions for the six turtles

        # Initialize each contestant and place them at their starting positions
        for i in range(len(y_positions)):
            contestant = Contestant(color=COLORS[i], start_x=start_x, start_y=y_positions[i])
            self.contestants.append(contestant)

    # Method to run the race
    def start_race(self):
        while True:
            for contestant in self.contestants:
                contestant.turtle.speed(randint(1, 10))
                # Move each turtle forward a random distance (1-10 units)
                contestant.turtle.fd(randint(1, 10))
                # Check if any turtle has reached the finish line (x = 220)
                if contestant.turtle.xcor() >= 220:
                    return contestant.turtle.pencolor()  # Return the winner's color
                    # return contestant.turtle.color()[0]  # Return the winner's color
                #color() - returns the current pencolor and the current fillcolor as a pair of color specification strings as are returned by pencolor and fillcolor.
# Set up the screen
screen = Screen()
screen.setup(width=500, height=400)

# Prompt the user to enter their bet on which turtle will win
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Only start the race if the user has placed a bet
if user_bet:
    race = Race()                     # Create a Race object
    winning_color = race.start_race()  # Start the race and get the winner's color

    # Announce the result
    if winning_color == user_bet:
        print(f"Congratulations! The {winning_color} turtle won!")
    else:
        print(f"The {winning_color} turtle won. Better luck next time!")

# Keep the window open until the user closes it
screen.mainloop()

#
# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
#
# class Contestant:
#     def __init__(self, color, x_coordinate, y_coordinate):
#         self.turtle = Turtle()
#         self.turtle.shape("turtle")
#         self.turtle.penup()
#         self.turtle.color(color)
#         self.turtle.goto(x=x_coordinate, y=y_coordinate)
#
#
# class Race:
#     def __init__(self):
#         self.contestants = []
#         y_positions = [70, 40, 10, -20, -50, -80]
#         for i in range(len(COLORS)):
#             contestant = Contestant(color=COLORS[i], x_coordinate=-230, y_coordinate=y_positions[i])
#             self.contestants.append(contestant)
#
#     def run(self):
#         while True:
#             for contestant in self.contestants:
#                 contestant.turtle.speed(randint(1, 10)) #Randomize animation speed
#                 contestant.turtle.fd(randint(1, 10)) #Randomize forward movement
#                 if contestant.turtle.xcor() >= 220:
#                     return contestant.turtle.color()[0]  # Get color name
#
#
# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
#
# if user_bet:
#     race = Race()
#     winner_color = race.run()
#
#     if winner_color == user_bet:
#         print(f"Congratulations! The {winner_color} turtle won!")
#     else:
#         print(f"The {winner_color} turtle won. Better luck next time!")
#
# screen.mainloop()
