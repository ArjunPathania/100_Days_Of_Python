import random as rand

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Easy version
password = ""
for i in range(nr_letters):
    password += rand.choice(letters)
for i in range(nr_numbers):
    password += rand.choice(numbers)
for i in range(nr_symbols):
    password += rand.choice(symbols)

print(f"Easy Password: {password}")

# Hard version
password_list = []
for i in range(nr_letters):
    password_list.append(rand.choice(letters))
for i in range(nr_numbers):
    password_list.append(rand.choice(numbers))
for i in range(nr_symbols):
    password_list.append(rand.choice(symbols))

# Shuffle the password list
size = len(password_list)
for x in range(size):
    pos = rand.randint(0, size - 1)
    password_list[x], password_list[pos] = password_list[pos], password_list[x]

# Join the list into a single string
hard_password = ''.join(password_list)
print(f"Hard Password: {hard_password}")
