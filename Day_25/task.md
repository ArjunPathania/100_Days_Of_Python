
---

# Task.md

## U.S. States Game Overview
This game is a geographical quiz on U.S. states, implemented with an OOP approach using the Python `Turtle` library and `pandas` for data handling. The player is prompted to guess the names of all 50 U.S. states. If the answer is correct, the state’s name is displayed at the appropriate location on a map. The game ends when the player has guessed all states or opts to quit.

## Code Structure and Classes

### 1. `State` Class
Represents a U.S. state with its name and coordinates.

- **Attributes**:
  - `name`: The name of the state.
  - `x`, `y`: The x and y coordinates of the state on the map.
  - `turtle`: A turtle object to display the state name.

- **Methods**:
  - `display_name()`: Moves the turtle to the state’s coordinates and writes the state name.

### 2. `StateGame` Class
Controls the main game flow, manages game states, and tracks guessed states.

- **Attributes**:
  - `screen`: The game screen where the U.S. map and states will be displayed.
  - `map_image`: The U.S. map background image.
  - `state_data`: A DataFrame containing state names and their coordinates from `50_states.csv`.
  - `guessed_states`: A list to store correctly guessed states.
  - `total_states`: The total number of states (50).
  - `guessed_count`: Counter for correctly guessed states.

- **Methods**:
  - `get_state_data(state_name)`: Retrieves the coordinates for a given state name from `state_data`.
  - `start_game()`: The main game loop that prompts the player to enter state names and updates the screen accordingly. If the player types "Exit," the game shows the missed states.
  - `show_missed_states()`: Displays a list of states that the player missed.

## Task Breakdown

1. **Set up the Screen and Map**:
   - Import and set up the `Screen` and `Turtle` objects to display the U.S. map.

2. **Implement the `State` Class**:
   - Create a `State` class to represent each state with attributes for the name and coordinates.
   - Add a `display_name` method to write the state's name at its corresponding position on the map.

3. **Implement the `StateGame` Class**:
   - Create a `StateGame` class to handle game operations.
   - Load state data from `50_states.csv` using `pandas`.
   - Define `start_game()` to manage user input and display guessed states.
   - Track guessed states and count to ensure all states are covered before the game ends.

4. **Game Flow in `start_game()`**:
   - Prompt the user for a state name in each iteration.
   - Validate the input to check if it’s a valid and unguessed state.
   - Display the state on the map if guessed correctly and update the counter.
   - Allow the user to exit the game by typing "Exit" and display missed states.

5. **Display Missed States**:
   - Show the list of missed states if the player exits before guessing all states.

6. **Test the Game**:
   - Run the game, ensuring the correct states appear on the map as guessed.
   - Verify that the game correctly handles invalid or repeated entries.

---