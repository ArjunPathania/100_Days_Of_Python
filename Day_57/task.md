# Name Guessing Project

## Overview
This project is a Flask-based web application that uses APIs to guess a person's age and gender based on their name. It demonstrates the integration of Flask, API requests, and template rendering for a dynamic web experience.

---

## Objectives
1. Create a Flask application with multiple routes.
2. Use APIs (`Agify` and `Genderize`) to fetch data based on user input.
3. Dynamically render HTML templates with the fetched data.

---

## Requirements
- **Python** with Flask installed.
- Knowledge of using Flask to create routes and render templates.
- Familiarity with handling API requests using the `requests` library.

---

## Steps to Complete the Project

### 1. **Setup the Environment**
   - Install Flask:
     ```bash
     pip install flask
     ```
   - Install `requests` for API calls:
     ```bash
     pip install requests
     ```

### 2. **Project Structure**
   - Create the following folder structure:
     ```
     /static
         (Optional: Add CSS/JS files here if needed)
     /templates
         index.html
         guess.html
     app.py
     ```

### 3. **Build the Flask App**
   - Import necessary libraries and initialize a Flask app.
   - Define two routes:
     - `/`: Home page with a welcome message or instructions.
     - `/guess/<string:name>`: Fetches and displays guessed age and gender based on the name.

### 4. **API Integration**
   - Use the `Agify` API to predict the age of a given name.
   - Use the `Genderize` API to predict the gender of the same name.
   - Handle API errors using `raise_for_status()`.

### 5. **Create HTML Templates**
   - **index.html**: 
     - Display a brief introduction about the project.
     - Provide instructions on how to use the `/guess/<name>` endpoint.
   - **guess.html**:
     - Display the guessed age and gender.
     - Include the user's name dynamically using template variables.

### 6. **Run the Application**
   - Run the Flask app:
     ```bash
     python app.py
     ```
   - Open the app in your browser (default: `http://127.0.0.1:5000/`).

---

## Features
- Dynamic age and gender prediction based on name input.
- Interactive route with personalized data rendering.
- Simple and clean HTML design for easy user interaction.

---

## Challenges
- Handling API rate limits and errors.
- Validating user input to ensure names are valid.
- Ensuring compatibility with different Flask versions.

---

## Bonus Features
- Add a **form** on the home page to input names and dynamically redirect to the `/guess/<name>` route.
- Style the application using **CSS** or a frontend framework like Bootstrap.
- Cache API responses to reduce redundant calls.

---

## Example Output
### Input: `/guess/John`
- **Guessed Age**: 30
- **Guessed Gender**: Male

### Input: `/guess/Sarah`
- **Guessed Age**: 25
- **Guessed Gender**: Female

---

## Next Steps
- Deploy the application to a platform like Heroku or Render.
- Extend functionality to include more APIs for additional predictions.
- Add user input validation and error messages.
