# Task Documentation for Flask Authorization Webapp

This document outlines the tasks and implementation details for the Flask-based authorization web application.

## Overview
The web application provides user authentication and authorization functionalities, including user registration, login, protected routes, and file downloads for authenticated users. It utilizes Flask, SQLAlchemy, and Flask-Login for handling the backend logic.

---

## Tasks

### 1. **Setup Flask Application**
- **Goal**: Initialize the Flask application and configure necessary extensions.
- **Steps**:
  - Initialize a Flask app.
  - Set a secret key for session management.
  - Configure the SQLAlchemy database.
  - Initialize Flask-Login for user session management.

---

### 2. **Database Configuration**
- **Goal**: Set up the database using SQLAlchemy and create a `User` model.
- **Steps**:
  - Define a `DeclarativeBase` for SQLAlchemy.
  - Create a `User` model with fields: `id`, `email`, `password`, and `name`.
  - Use `sqlite:///users.db` as the database URI.
  - Ensure the `email` field is unique to prevent duplicate registrations.
  - Initialize the database and create tables.

---

### 3. **User Registration**
- **Goal**: Allow new users to register by providing a name, email, and password.
- **Steps**:
  - Hash passwords using `werkzeug.security.generate_password_hash`.
  - Check if the email is already registered.
  - Store new users in the database.
  - Log in the user after successful registration.
  - Flash messages for feedback (e.g., "Registration successful!" or "Email already exists!").

---

### 4. **User Login**
- **Goal**: Authenticate users using email and password.
- **Steps**:
  - Query the database to check if the user exists.
  - Verify the password using `werkzeug.security.check_password_hash`.
  - Log in the user upon successful authentication.
  - Flash messages for errors (e.g., "Email does not exist" or "Incorrect password").

---

### 5. **Protected Routes**
- **Goal**: Restrict access to certain pages for authenticated users only.
- **Routes**:
  - `/secrets`: A page accessible only to logged-in users.
  - `/download`: A route to download a file, requiring authentication.
- **Steps**:
  - Use `@login_required` decorator from Flask-Login.
  - Pass the user's authentication status (`logged_in`) to templates for conditional rendering.

---

### 6. **User Logout**
- **Goal**: Allow users to log out and terminate their session.
- **Steps**:
  - Use `logout_user` from Flask-Login to clear the session.
  - Redirect users to the home page after logout.

---

### 7. **Templates**
- **Goal**: Provide HTML templates for the application’s pages.
- **Required Templates**:
  - `index.html`: The home page with login status.
  - `register.html`: User registration form.
  - `login.html`: User login form.
  - `secrets.html`: A page displaying protected content for authenticated users.
- **Steps**:
  - Use `Jinja2` templating engine for dynamic content rendering.
  - Pass variables like `logged_in` and `name` to templates.

---

### 8. **File Download Functionality**
- **Goal**: Enable authenticated users to download a protected file.
- **Steps**:
  - Use `send_from_directory` to serve files from the `static` directory.
  - Restrict access to the `/download` route using `@login_required`.
  - Specify the file path (`static/files/cheat_sheet.pdf`).

---

## Improvements and Future Enhancements
- Add email verification for user registration.
- Implement password reset functionality.
- Use environment variables for sensitive configurations (e.g., secret key, database URI).
- Add CAPTCHA or reCAPTCHA for enhanced security.
- Integrate with an external authentication provider (e.g., Google, Facebook).
- Enhance UI/UX of templates with a frontend framework like Bootstrap.

---

## Running the Application
- **Steps**:
  1. Install dependencies: `pip install flask flask-sqlalchemy flask-login werkzeug`.
  2. Run the app: `python <filename>.py`.
  3. Access the app at `http://127.0.0.1:5000/`.
- **Dependencies**:
  - Flask
  - Flask-SQLAlchemy
  - Flask-Login
  - Werkzeug

---

## Conclusion
This Flask application demonstrates a basic yet secure implementation of user authentication and authorization, with opportunities for scaling and adding advanced features.

