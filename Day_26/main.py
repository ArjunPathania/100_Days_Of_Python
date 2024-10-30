import pandas as pd
df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {value.letter:value.code for (key,value) in df.iterrows()}
# print(nato_dict)

#.
user_input = input("Enter a string:").upper()
user_list = list(user_input)
user_phonetic_string_list = [nato_dict[alphabet] for alphabet in user_list]
print(user_phonetic_string_list)

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}
#
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