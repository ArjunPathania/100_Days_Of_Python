# Project Tasks

## 1. Database Setup
- **Task**: Create and configure the `posts.db` SQLite database to store blog posts.
- **Details**: 
  - Used SQLAlchemy to configure a database.
  - Created a `BlogPost` model to represent the posts.
  - Ran the `db.create_all()` method to initialize the database.
  - The `posts.db` database stores fields like title, subtitle, date, body, author, and image URL.

## 2. Loading Posts from Database
- **Task**: Load blog posts from the database instead of using an API.
- **Details**:
  - Implemented a route `/` to display all blog posts.
  - Fetched posts from the database using SQLAlchemy’s `db.session.execute(db.select(BlogPost))`.
  - Displayed posts in `index.html` by iterating over the results.

## 3. Add Blog Post Functionality (Using Flask-WTF and CKEditor)
- **Task**: Allow users to add new blog posts via a form with Flask-WTF and CKEditor.
- **Details**:
  - Created a `BlogForm` using Flask-WTF to handle blog post creation.
  - Integrated CKEditor for rich text editing in the `body` field.
  - Added validation for form fields, including title, subtitle, author, image URL, and body.
  - Used `clean` from the `bleach` library to sanitize the content in the CKEditor to avoid unwanted HTML tags.
  - Successfully added posts to the database on form submission, with success and error flash messages.

## 4. Edit Blog Post Functionality
- **Task**: Allow users to edit existing blog posts.
- **Details**:
  - Created a route `/edit-post/<int:post_id>` to handle editing of blog posts.
  - Prefilled the form fields with the existing blog post data for easy editing.
  - Used CKEditor for editing the blog post content.
  - Sanitize the content on form submission using `clean` from `bleach`.
  - Updated the blog post in the database upon successful form submission, with success and error flash messages.

## 5. Delete Blog Post Functionality
- **Task**: Allow users to delete blog posts from the database.
- **Details**:
  - Created a route `/delete/<int:post_id>` to handle the deletion of blog posts.
  - Used `db.session.delete()` to remove the selected post from the database.
  - Redirected to the main page after successful deletion.

## 6. Contact Form with Email Functionality
- **Task**: Implement a contact form for users to send messages.
- **Details**:
  - Created a `ContactForm` using Flask-WTF with fields like name, email, phone, and message.
  - Validated the form and sent the email using `smtplib`.
  - Stored email credentials securely using environment variables loaded with `dotenv`.
  - Upon successful form submission, sent the email to the designated address and displayed a success flash message.

## 7. Environment Variables Configuration
- **Task**: Load sensitive email credentials from environment variables.
- **Details**:
  - Used the `python-dotenv` library to load environment variables from a `.env` file.
  - Retrieved the `FROM_EMAIL`, `PASSWORD`, and `TO_EMAIL` values from the environment variables to avoid hardcoding sensitive information in the code.

## 8. Project Setup and Configuration
- **Task**: Set up the Flask project and integrate necessary extensions.
- **Details**:
  - Integrated Flask, Flask-WTF, Flask-Bootstrap, Flask-CKEditor, and SQLAlchemy into the project.
  - Configured the app with necessary settings, including the secret key and CKEditor configurations.
  - Set up routes for the homepage, individual post pages, about page, contact form, etc.
  - Ensured the app runs with `debug=True` for easier development.

## 9. UI/UX Improvements
- **Task**: Improve the user interface and user experience using Flask-Bootstrap.
- **Details**:
  - Integrated Flask-Bootstrap to provide a responsive design and enhance the UI.
  - Styled forms and pages using Bootstrap components to ensure a modern, mobile-friendly design.

## 10. Final Testing
- **Task**: Conduct testing to ensure the application works correctly.
- **Details**:
  - Tested adding, editing, and deleting blog posts.
  - Verified that the contact form sends emails successfully.
  - Ensured proper handling of form validation and flash messages.

## Notes:
- You can run the application with `flask run` on port 5003.
- Ensure that the `.env` file contains the correct email credentials.
