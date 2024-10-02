import random
import hangman_words
import hangman_art

lives = 6
word_list = hangman_words.word_list
logo = hangman_art.logo
print(logo)

chosen_word = random.choice(word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""

    if guess in correct_letters:
        print(f"You have already guessed {guess}")

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not int he word. You loose a life.")

    if guess not in chosen_word:
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************\nThe correct word was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    stages = hangman_art.stages
    print(stages[lives])
