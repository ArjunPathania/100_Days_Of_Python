import random
import art


def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # Ace = 11, Face cards = 10
    return random.choice(cards)


def calculate_score(cards):
    """Calculates and returns the score of a hand of cards"""
    # Natural Blackjack condition
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents Blackjack

    # Adjust for Ace being 11 or 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare_scores(user_score, computer_score):
    """Compares user's score against computer's score and returns the result"""
    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """Main function to play a game of Blackjack"""
    print(art.logo)

    # Deal initial two cards to both user and computer
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    # Calculate initial scores
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    is_game_over = False

    while not is_game_over:
        # Show user and computer's first card
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check for Blackjack or user bust
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Let the user decide whether to draw another card
            user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_choice == "y":
                user_cards.append(deal_card())
                user_score = calculate_score(user_cards)  # Recalculate user score
            else:
                is_game_over = True

    # Computer's turn: draws cards if score is less than 17 and user hasn't busted
    if user_score <= 21:
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)  # Recalculate computer score

    # Final result
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))


# Game loop
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
