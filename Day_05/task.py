import random as rand
from email.policy import default

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#easy version
password = ""
for i in range(0,nr_letters):
    password = password + rand.choice(letters)
for i in range(0,nr_numbers):
    password = password + rand.choice(numbers)
for i in range(0,nr_symbols):
    password = password + rand.choice(symbols)
print(password)

#hard version

password = []
for i in range(0,nr_letters):
    password.append(rand.choice(letters))
for i in range(0,nr_numbers):
    password.append(rand.choice(numbers))
for i in range(0,nr_symbols):
    password.append(rand.choice(symbols))

size = nr_numbers+nr_letters +nr_symbols

#shuffle list using randomization
for x in range(0,size):
    pos = rand.randint(0,size-1)
    element1 = password[pos]
    password[pos] = password[x]
    password[x] = element1

# # Assuming 'password' is the list you want to shuffle and 'size' is its length
# for x in range(size):
#     pos = rand.randint(0, size - 1)
#     # Swap elements
#     password[x], password[pos] = password[pos], password[x]

hard_password= ""
for x in password:
    hard_password = hard_password + str(x)

print(hard_password)
