import pandas as pd

# Load the NATO phonetic alphabet data
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter: value.code for (key, value) in df.iterrows()}

# Function to get phonetic code words
def generate_phonetic():
    user_input = input("Enter a string: ").upper()
    try:
        user_phonetic_string_list = [nato_dict[alphabet] for alphabet in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        return generate_phonetic()  # Recursively prompt again if invalid input
    else:
        print(user_phonetic_string_list)

generate_phonetic()



# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# import pandas
#
# data = pandas.read_csv("nato_phonetic_alphabet.csv")
#
# phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# print(phonetic_dict)
#
#
# word = input("Enter a word: ").upper()
# output_list = [phonetic_dict[letter] for letter in word]
# print(output_list)