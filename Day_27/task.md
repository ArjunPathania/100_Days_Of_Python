
---

# Task.md

## Task Overview
The goal is to create a graphical user interface (GUI) application that converts miles to kilometers. This application will take user input in miles, perform the conversion to kilometers, and display the result.

### Task Breakdown

1. **Create the Main Window**:
   - Initialize the main window using the `Tk()` class from the `tkinter` library.
   - Set the window title to "Mile to Km Converter".
   - Add padding around the window’s contents for a cleaner layout.

2. **Define Conversion Function**:
   - Create a function named `convert_miles_to_km` to handle the conversion.
   - Retrieve and convert the input from the miles entry field to a float.
   - Convert the miles value to kilometers using the formula (1 mile ≈ 1.60934 km).
   - Display the result in the kilometers result label.
   - Handle invalid input by displaying an error message.

3. **Add Miles Input Field**:
   - Add an entry widget for users to input the miles value.
   - Set the width of the entry field and position it within the grid layout.

4. **Add Labels**:
   - Add a label to indicate the input unit ("Miles").
   - Add a label with the text "is equal to" to show the relationship between miles and kilometers.
   - Add a result label for displaying the converted kilometers, initialized to "0".
   - Add a label to indicate the output unit ("Km").

5. **Add Calculate Button**:
   - Add a button labeled "Calculate" that calls the `convert_miles_to_km` function when clicked.

6. **Run the Application**:
   - Start the main event loop to display the window and handle user interactions.

---
