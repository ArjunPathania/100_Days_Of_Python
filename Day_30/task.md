# Task.md: Password Manager Project

## Project Overview
The **Password Manager** application is a GUI-based tool designed to manage and store user credentials securely. It includes features such as password generation, validation, saving, searching, and toggling password visibility.

---

## Features and Functionality
### 1. **Password Validation**
   - **Conditions:**
     - Minimum length: 8 characters.
     - At least 2 symbols and 2 numbers.
   - **Feedback:** Displays error messages for weak passwords via `messagebox`.

### 2. **Password Generator**
   - Randomly generates a secure password consisting of:
     - 8–12 letters (upper and lowercase).
     - 2–4 symbols.
     - 2–4 numbers.
   - Autofill the password field and copies it to the clipboard.

### 3. **Save Password**
   - **Input Fields:**
     - Website Name
     - Email/Username
     - Password
   - Saves credentials to `saved_passwords.json`.
   - Handles file creation, reading, updating, and writing.
   - User confirmation before saving.
   - Clears input fields after saving.

### 4. **Search Password**
   - Searches `saved_passwords.json` for the entered website.
   - Displays credentials if found, or shows an error if not.
   - Copies credentials to the clipboard if found.

### 5. **Toggle Password Visibility**
   - Allows users to show or hide the password in the password field.

### 6. **User Interface**
   - Created using **Tkinter**.
   - Includes labels, entries, and buttons for interactivity.
   - Features a logo display.

---

## UI Components
| **Component** | **Description**                                                  |
|---------------|------------------------------------------------------------------|
| `Canvas`      | Displays the logo image.                                         |
| `Label`       | Used for field descriptions.                                     |
| `Entry`       | Input fields for website, username, and password.                |
| `Button`      | Interactive buttons for actions (Search, Add, Generate, Toggle). |

---

## Required Libraries
- **tkinter**: For GUI components.
- **random**: To generate random passwords.
- **string**: To access character sets for password generation.
- **pyperclip**: To copy generated passwords to the clipboard.
- **json**: To handle saving and retrieving data.

---

## File Handling
- **File:** `saved_passwords.json`
- **Structure:**
  ```json
  {
      "website_name": {
          "username": "example_username",
          "password": "example_password"
      }
  }
  ```
- Handles errors like missing or corrupt files gracefully.

---

## Error Handling
| **Scenario**                      | **Error Message**                                     |
|-----------------------------------|-------------------------------------------------------|
| Weak password                     | "Password is too short" or "Password must include..." |
| Empty fields                      | "Please make sure you haven't left any fields empty." |
| File not found during search/save | "The saved passwords file does not exist."            |
| Data not found for a website      | "No match found for the specified website."           |
| JSON decoding error               | "Error reading saved passwords file."                 |

---

## To-Do Enhancements
1. **Add Encryption:**
   - Encrypt passwords before saving and decrypt them during retrieval for added security.
2. **UI Improvements:**
   - Enhance visual design with modern styling.
3. **Sorting and Filtering:**
   - Allow users to sort and filter saved entries for easier management.
4. **Mobile/Desktop App Integration:**
   - Extend the project to support mobile or desktop apps for seamless access.

---

## Setup and Execution
1. Ensure Python is installed.
2. Install required packages:
   ```bash
   pip install pyperclip
   ```
3. Place a `logo.png` file in the working directory.
4. Run the script:
   ```bash
   python password_manager.py
   ```

---