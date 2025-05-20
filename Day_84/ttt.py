board = [' ' for _ in range(9)]

def print_board():
    print("\n")
    print(f"|{board[0]}|{board[1]}|{board[2]}|")
    print(f"|{board[3]}|{board[4]}|{board[5]}|")
    print(f"|{board[6]}|{board[7]}|{board[8]}|")
    print("\n")

def check_winner(player):
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    for combo in win_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False

def is_draw():
    return ' ' not in board

def play_game():
    current_player = 'X'
    print("Welcome to Tic Tac Toe!")
    print("Enter positions 1-9 to make your move.")
    print_board()

    while True:
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
                continue
        except ValueError:
            print("Please enter a number between 1 and 9.")
            continue

        board[move] = current_player
        print_board()

        if check_winner(current_player):
            print(f"🎉 Player {current_player} wins!")
            break
        elif is_draw():
            print("It's a draw!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play_game()
