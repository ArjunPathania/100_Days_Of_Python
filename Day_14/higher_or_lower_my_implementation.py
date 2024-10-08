import random
import game_data
import art


def generate_choice():
    index = random.randint(0,49)
    name = game_data.data[index]["name"]
    description = game_data.data[index]["description"]
    country = game_data.data[index]["country"]
    return [name,description,country,index]

def compare_choice(a,b):
    if game_data.data[a]["follower_count"]>game_data.data[b]["follower_count"]:
        return 'a'
    else:
        return 'b'


def game():
    print(art.logo)
    player_score = 0
    game_over = False
    option_a = generate_choice()
    option_b = generate_choice()
    while not game_over:
        print(f"Compare A: {option_a[0]},a {option_a[1]}, from {option_a[2]}.")
        print(art.vs)
        print(f"against B: {option_b[0]},a {option_b[1]}, from {option_b[2]}.")
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if compare_choice(option_a[3], option_b[3]) == user_choice:
            player_score += 1
            print("\n" * 20)
            print(art.logo)
            print(f"You're right! Current score: {player_score}.")
            option_a = option_b
            option_b = generate_choice()
        else:
            game_over = True
            print(f"Sorry, that's wrong. Final score: {player_score}")

game()