import time
import os
from tkinter import *
from playsound import playsound

# ---------------------------- Audio Setup --------------------------- #
BASE_DIR = os.path.dirname(__file__)
LONG_AUDIO = os.path.join(BASE_DIR, 'long.mp3')
SHORT_AUDIO = os.path.join(BASE_DIR, 'short.mp3')

# ---------------------------- Morse Code Dictionary ------------------ #
MORSE_CODE_DICT = {
    'A': '•-', 'B': '-•••', 'C': '-•-•', 'D': '-••', 'E': '•',
    'F': '••-•', 'G': '--•', 'H': '••••', 'I': '••', 'J': '•---',
    'K': '-•-', 'L': '•-••', 'M': '--', 'N': '-•', 'O': '---',
    'P': '•--•', 'Q': '--•-', 'R': '•-•', 'S': '•••', 'T': '-',
    'U': '••-', 'V': '•••-', 'W': '•--', 'X': '-••-', 'Y': '-•--',
    'Z': '--••', '1': '•----', '2': '••---', '3': '•••--',
    '4': '••••-', '5': '•••••', '6': '-••••', '7': '--•••',
    '8': '---••', '9': '----•', '0': '-----', ',': '--••--',
    '.': '•-•-•-', '?': '••--••', '!': '-•-•--'
}
REVERSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


# ---------------------------- Functions ------------------------------ #
def english_to_morse(event=None):
    for label in morse_labels.values():
        label.config(bg='white', fg='black')

    text = english_input.get('1.0', END).strip().upper()
    morse_result = []

    for char in text:
        if char in MORSE_CODE_DICT:
            morse_result.append(MORSE_CODE_DICT[char])
            morse_labels[char].config(bg='black', fg='white')
        elif char == ' ':
            morse_result.append('')  # Word space

    morse_output.delete('1.0', END)
    morse_output.insert('1.0', ' '.join(morse_result))


def morse_to_english(event=None):
    text = morse_output.get('1.0', END).strip().replace('.', '•')
    words = text.split('  ')  # Word space: double space
    decoded_message = []

    for word in words:
        letters = word.strip().split()
        try:
            decoded_word = ''.join(REVERSE_DICT[code] for code in letters)
            decoded_message.append(decoded_word)
        except KeyError:
            decoded_message.append('[?]')  # Invalid Morse

    english_input.delete('1.0', END)
    english_input.insert('1.0', ' '.join(decoded_message))


def play_sound():
    codes = morse_output.get('1.0', END).strip()
    for symbol in codes:
        if symbol == '•':
            playsound(SHORT_AUDIO)
        elif symbol == '-':
            playsound(LONG_AUDIO)
        elif symbol == ' ':
            time.sleep(0.3)
        time.sleep(0.1)


# ---------------------------- UI Setup ------------------------------- #
window = Tk()
window.title('Text to Morse Code Converter')
window.config(padx=10, pady=10, bg='black')
window.attributes('-alpha', 0.9)

# Morse Code Grid
morse_labels = {}
row = 0
col = 0
for char, code in MORSE_CODE_DICT.items():
    label = Label(text=f"{char}\n{code}", width=5, height=2, relief='solid', borderwidth=1, bg='white')
    label.grid(row=row, column=col, padx=1, pady=1)
    morse_labels[char] = label
    col += 1
    if col >= 10:
        col = 0
        row += 1

# English Input
english_input = Text(width=50, height=5)
english_input.grid(row=row + 1, column=0, columnspan=10, pady=10, sticky='EW')
english_input.insert('1.0', 'Enter English to Encode')
english_input.bind('<KeyRelease>', english_to_morse)

# Morse Output/Input
morse_output = Text(width=50, height=5)
morse_output.grid(row=row + 2, column=0, columnspan=10, pady=10, sticky='EW')
morse_output.insert('1.0', 'Enter Morse Code to Decode (use space for letters, double space for words)')
morse_output.bind('<KeyRelease>', morse_to_english)

# Play Button
play_button = Button(text='Play Morse Sound', command=play_sound, relief='raised', height=2)
play_button.grid(row=row + 3, column=0, columnspan=10, pady=10, sticky='EW')

window.mainloop()
