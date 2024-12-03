# Task.md: Flash Card Language Learning App

## Project Overview
This project is a **Flash Card Language Learning App** that helps users learn French-to-English translations. The app features an interactive interface to display French words, their English meanings, and tracks progress by marking learned words.

---

## Features and Functionality

### 1. **Flash Card Display**
   - Displays a French word initially.
   - Flips the card after 3 seconds to reveal the English translation.

### 2. **Word Tracking**
   - Tracks unlearned words using `words_to_learn.csv`.
   - Updates the list by removing words marked as "known."

### 3. **Persistent Progress**
   - Saves the updated list of unlearned words to `words_to_learn.csv` for subsequent sessions.
   - If `words_to_learn.csv` is missing, loads words from the default dataset (`translated_fr_to_en_dict.csv`).

### 4. **Buttons for Interaction**
   - **Right Button:** Marks the current word as "known" and updates the dataset.
   - **Wrong Button:** Skips the current word and shows a new one.

---

## UI Components

| **Component**   | **Description**                                          |
|-----------------|----------------------------------------------------------|
| **Canvas**      | Displays flash cards and text (language and word).       |
| **Text Fields** | Shows the language ("French" or "English") and the word. |
| **Buttons**     | Allows marking words as known or skipping words.         |

---

## Data Handling

### 1. **Files Used**
   - **`translated_fr_to_en_dict.csv`**: Default dataset of French-to-English translations.
   - **`words_to_learn.csv`**: Tracks unlearned words. Created or updated dynamically.

### 2. **Data Format**
   - **CSV Structure:**
     ```csv
     French,English
     mot1,word1
     mot2,word2
     ```

### 3. **Error Handling**
   - If `words_to_learn.csv` is missing, the app automatically loads from `translated_fr_to_en_dict.csv`.

---

## Core Functions

| **Function Name**   | **Description**                                                                           |
|---------------------|-------------------------------------------------------------------------------------------|
| `next_card()`       | Displays a new French word on the card and flips it after 3 seconds.                      |
| `flip_card()`       | Flips the card to show the English translation of the word.                               |
| `mark_as_known()`   | Marks the current word as learned, removes it from the dataset, and updates the CSV file. |
| `disable_buttons()` | Temporarily disables the "right" and "wrong" buttons.                                     |
| `enable_buttons()`  | Re-enables the "right" and "wrong" buttons after the card flip.                           |

---

## UI Setup

### Main Window
- Background color: `#B1DDC6`
- Padding: 50px on all sides.

### Flash Card
- **Front Side:** Displays the French word.
- **Back Side:** Displays the English translation.

### Buttons
- **Wrong Button:** Skips the current word.
- **Right Button:** Marks the current word as learned.

---

## Enhancements To-Do

1. **Additional Languages:**
   - Extend support for other language pairs.
   - Dynamically load datasets for selected languages.

2. **Gamification:**
   - Add a progress bar or scoring system to motivate learners.

3. **Speech Integration:**
   - Use text-to-speech to pronounce French words and translations.

4. **Mobile/Desktop Versions:**
   - Convert the app into a mobile or standalone desktop application.

---

## Setup and Execution

1. Ensure Python is installed.
2. Install required libraries:
   ```bash
   pip install pandas
   ```
3. Place the following files in the appropriate directories:
   - `translated_fr_to_en_dict.csv`: In `Data/fr_to_en_data/`.
   - `card_front.png`, `card_back.png`, `wrong.png`, `right.png`: In `Images/`.

4. Run the script:
   ```bash
   python flash_card_app.py
   ```
---