

---

# Task.md

## Task Overview
The objective is to build a converter that transforms user-inputted text into corresponding NATO phonetic code words. This will involve reading data from a CSV file containing the NATO phonetic alphabet, creating a dictionary of phonetic codes, and using it to translate each letter of the input.

### Task Breakdown

1. **Load the CSV File**:
   - Import the `pandas` library.
   - Read the file `nato_phonetic_alphabet.csv` to load the NATO phonetic alphabet data into a DataFrame. The file contains each letter and its associated phonetic code word.

2. **Create a Phonetic Code Dictionary**:
   - Use dictionary comprehension along with `DataFrame.iterrows()` to create a dictionary that maps each letter to its NATO phonetic code word. This dictionary will allow for efficient lookup of phonetic codes for each letter.

3. **Prompt User for Input**:
   - Take a string input from the user. Convert the input to uppercase to standardize matching with the dictionary.

4. **Convert Input Text to Phonetic Codes**:
   - Convert the user input into a list of individual letters.
   - Generate a list of NATO phonetic code words by replacing each letter in the input with its corresponding code word from the dictionary.

5. **Display the Result**:
   - Print the list of phonetic code words that correspond to the letters of the user input.

---
