# Password Manager Application

## Project Overview
This password manager application allows users to securely generate, store, and manage their passwords for different websites. The application features password validation, password generation, and a simple user interface built with Tkinter.

## Features
- **Password Generation**: Generate secure passwords with customizable parameters.
- **Password Validation**: Ensure passwords meet complexity requirements.
- **Password Storage**: Save passwords for different websites with user confirmation.
- **Duplicate Entry Check**: Prevent saving duplicate entries for the same website and username.
- **Password Visibility Toggle**: Show or hide the password in the input field.
- **Clipboard Copying**: Automatically copy generated passwords to the clipboard for easy use.

## Tasks

### 1. UI Setup
- [ ] Create a Tkinter window with appropriate titles and padding.
- [ ] Design the layout with labels, entry fields, and buttons for user interaction.

### 2. Password Generation
- [ ] Implement the `password_generator` function to generate random passwords based on defined criteria.
- [ ] Ensure the generated password includes letters, numbers, and symbols.

### 3. Password Validation
- [ ] Develop the `validation` function to check password strength.
- [ ] Ensure the password meets the minimum requirements (length, symbols, numbers).

### 4. Saving Passwords
- [ ] Create the `save_password` function to save user-entered credentials to a text file.
- [ ] Implement user confirmation before saving passwords.
- [ ] Add logic to check for existing entries in the text file to prevent duplicates.

### 5. Password Visibility Toggle
- [ ] Implement the `toggle_password_visibility` function to allow users to show/hide their passwords.
- [ ] Update the button text based on the visibility state.

### 6. Clipboard Functionality
- [ ] Use the `pyperclip` library to copy generated passwords to the clipboard automatically.

### 7. Error Handling
- [ ] Add error handling for file operations (e.g., file not found).
- [ ] Implement user feedback for empty fields, weak passwords, and save failures.

### 8. Testing
- [ ] Conduct thorough testing of all functionalities, including:
  - Password generation
  - Password validation
  - Saving and retrieving passwords
  - UI responsiveness

## Future Enhancements
- [ ] Implement password editing and deletion features.
- [ ] Add password strength indicators.
- [ ] Allow exporting/importing password entries.
- [ ] Enhance UI with themes or better layout options.

## Technologies Used
- Python
- Tkinter (for UI)
- Random (for password generation)
- String (for character sets)
- Pyperclip (for clipboard functionality)
