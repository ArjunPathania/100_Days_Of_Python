
---

# task.md

## Task Overview
The objective is to create personalized invitation letters by replacing a placeholder in a template letter with actual names from a list. Each letter will be saved in a designated "ReadyToSend" folder.

### Task Breakdown

1. **Read Template Letter**:
   - Open and read `starting_letter.txt` from the `Input/Letters` folder.
   - Store the contents in a variable (e.g., `starting_letter`).

2. **Load Names of Invitees**:
   - Open and read `invited_names.txt` from the `Input/Names` folder.
   - Store each line (name) from the file into a list (e.g., `invited_names`).

3. **Generate Personalized Letters**:
   - For each name in `invited_names`:
     - Remove any extra whitespace or newline characters.
     - Replace the `[name]` placeholder in `starting_letter` with the actual name.
     - Save each personalized letter as a new file in the `Output/ReadyToSend` folder with a unique filename, e.g., `letter_for_<name>.txt`.

4. **Write Letters to Files**:
   - Use a `for` loop to create and write each personalized letter to the appropriate location.
   - Ensure each file is saved separately with the invitee’s name included in the filename to prevent overwriting.

---