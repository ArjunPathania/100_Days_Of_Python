import random as rand
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

gameImages = [rock,paper,scissors]

print('"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."')
user_choice = int(input())

print(gameImages[user_choice])

print("Computer chose: ")
computer_choice = rand.randint(0, 2)
print(gameImages[computer_choice])

if user_choice > 3 and user_choice <0:
    print("You typed invalid number.  You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice == user_choice:
    print("It's a draw!")



# how I did it

# if computer_choice == 0:
#     print(rock)
# elif computer_choice == 1:
#     print(paper)
# else:
#     print(scissors)


# if usersChoice == 0:
#     if computer_choice == 0:
#         print("Draw")
#     elif computer_choice == 1:
#         print("Computer Wins")
#     elif computer_choice == 2:
#         print("You win!")
#
# if usersChoice == 1:
#     if computer_choice == 1:
#         print("Draw")
#     elif computer_choice == 2:
#         print("Computer Wins")
#     elif computer_choice == 0:
#         print("You win!")
#
# if usersChoice == 2:
#     if computer_choice == 2:
#         print("Draw")
#     elif computer_choice == 0:
#         print("Computer Wins")
#     elif computer_choice == 1:
#         print("You win!")

