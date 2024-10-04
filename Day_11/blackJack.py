#39. Build a program that simulates a basic text-based blackjack game against the computer.

import random

def create_deck():
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    deck = [{'suit': suit, 'value': value} for suit in suits for value in values]
    random.shuffle(deck)
    return deck

def card_value(card):
    if card['value'] in ['Jack', 'Queen', 'King']:
        return 10
    elif card['value'] == 'Ace':
        return 11
    else:
        return int(card['value'])

def calculate_hand_value(hand):
    value = sum(card_value(card) for card in hand)
    num_aces = sum(1 for card in hand if card['value'] == 'Ace')
    while value > 21 and num_aces:
        value -= 10
        num_aces -= 1
    return value

def display_hand(hand, hide_first_card=False):
    if hide_first_card:
        print("Dealer's hand:")
        print("X", hand[1]['value'])
    else:
        print("Hand:")
        for card in hand:
            print(card['value'], card['suit'])

def blackjack_game():
    deck = create_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print("Welcome to Blackjack!")

    display_hand(player_hand)
    display_hand(dealer_hand, hide_first_card=True)

    while True:
        action = input("Do you want to (h)it or (s)tand? ")
        if action.lower() == 'h':
            player_hand.append(deck.pop())
            print("You drew:")
            print(player_hand[-1]['value'], player_hand[-1]['suit'])
            if calculate_hand_value(player_hand) > 21:
                print("You bust! Dealer wins.")
                return
        elif action.lower() == 's':
            break

    print("\nDealer's turn")
    display_hand(dealer_hand)
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print("\nDealer drew:")
        print(dealer_hand[-1]['value'], dealer_hand[-1]['suit'])

    player_score = calculate_hand_value(player_hand)
    dealer_score = calculate_hand_value(dealer_hand)

    print("\nYour score:", player_score)
    print("Dealer's score:", dealer_score)

    if player_score > 21:
        print("You bust! Dealer wins.")
    elif dealer_score > 21:
        print("Dealer busts! You win.")
    elif player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins.")
    else:
        print("It's a tie.")

# Start the game
blackjack_game()