from turtle import Turtle, Screen
import pandas as pd


class State:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()

    def display_name(self):
        self.turtle.goto(self.x, self.y)
        self.turtle.write(arg=self.name, move=False, align="center", font=("Arial", 8, "normal"))


class StateGame:
    def __init__(self):
        self.screen = Screen()
        self.screen.title("U.S. States Game")
        self.screen.addshape("blank_states_img.gif")
        self.map_image = Turtle(shape="blank_states_img.gif")

        self.state_data = pd.read_csv("50_states.csv")
        self.guessed_states = []
        self.total_states = len(self.state_data)
        self.guessed_count = 0

    def get_state_data(self, state_name):
        """Retrieve coordinates for a given state name."""
        state_row = self.state_data[self.state_data.state == state_name]
        if not state_row.empty:
            x, y = state_row.iloc[0]['x'], state_row.iloc[0]['y']
            return x, y
        return None, None

    def start_game(self):
        while self.guessed_count < self.total_states:
            answer_state = self.screen.textinput(
                title=f"{self.guessed_count}/{self.total_states} States Correct",
                prompt="What's another state? Type 'Exit' to quit"
            ).title()

            if answer_state == "Exit":
                self.show_missed_states()
                break

            if answer_state in self.guessed_states:
                self.screen.textinput(title="Oops!", prompt="Already guessed that state. Try another.")
                continue

            if answer_state in self.state_data.state.values:
                x, y = self.get_state_data(answer_state)
                if x is not None and y is not None:
                    state = State(answer_state, x, y)
                    state.display_name()
                    self.guessed_states.append(answer_state)
                    self.guessed_count += 1
            else:
                self.screen.textinput(title="Oops!", prompt="That's not a valid state. Try again.")

    def show_missed_states(self):
        missed_states = [state for state in self.state_data.state if state not in self.guessed_states]
        print("Missed states:", missed_states)


# Run game
game = StateGame()
game.start_game()
game.screen.mainloop()
