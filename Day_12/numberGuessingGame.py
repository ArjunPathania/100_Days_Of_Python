# import random
# import art
# print(art.logo)
# print("Welcome to the Number Guessing Game!")
# number = random.randint(1,100)
# print("I'm thinking of a number between 1 and 100.")
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")
# if difficulty == 'easy':
#     chances = 10
#     print("You have 10 attempts remaining to guess the number.")
# else:
#     chances = 5
#     print("You have 5 attempts remaining to guess the number.")
# while chances !=0:
#     guess = int(input("Make a guess:"))
#     if guess == number:
#         print(f"You got it! The answer was {number}.")
#         break
#     elif guess > number:
#         chances-=1
#         if chances == 0:
#             break
#         print(f"Too high.\nGuess again.\nYou have {chances} attempts remaining to guess the number.")
#     elif guess < number:
#         chances-=1
#         if chances == 0:
#             break
#         print(f"Too low.\nGuess again.\nYou have {chances} attempts remaining to guess the number.")
#
# if chances == 0:
#     print("You've run out of guesses, you lose.")
import random
import art
EASY_LEVEL_CHANCES = 10
HARD_LEVEL_CHANCES = 5

def check_answer(user_guess,actual_answer,turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")

def set_difficulty():
    if input("Choose a difficulty. Type 'easy' or 'hard':") == "easy":
        return EASY_LEVEL_CHANCES
    else:
        return HARD_LEVEL_CHANCES




def number_guessing_game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1,100)
    turns = set_difficulty()
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
        elif guess != answer:
            print("Guess again.")

number_guessing_game()
