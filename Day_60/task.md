# Task: Add HTML Forms to the Flask Website and Implement the Contact Page

## Objective
Enhance the existing Flask web application by adding appropriate HTML forms and ensuring that the contact page functions correctly. This involves:
1. Creating or updating HTML templates for forms.
2. Implementing the backend logic to process form submissions.
3. Ensuring the email functionality works as intended.

---

## Steps

### 1. Add HTML Forms to `contact.html`
#### Tasks:
- Create an HTML form for the contact page with the following fields:
  - **Name** (text input, required)
  - **Email** (email input, required)
  - **Phone** (text input, optional)
  - **Message** (textarea, required)
- Include a submit button labeled "Send Message".

#### Example HTML Code:
```html
<form method="POST">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name" required>

  <label for="email">Email:</label>
  <input type="email" id="email" name="email" required>

  <label for="phone">Phone:</label>
  <input type="text" id="phone" name="phone">

  <label for="message">Message:</label>
  <textarea id="message" name="message" required></textarea>

  <button type="submit">Send Message</button>
</form>
```
- Include logic to display a success message (`msg_sent=True`) if the form submission is successful.

### 2. Verify and Update Backend Logic
#### Tasks:
- Ensure the `@app.route("/contact", methods=["GET", "POST"])` endpoint processes the form submission.
- Use the `request.form` object to extract user input from the form.
- Verify the `send_email` function sends emails with the extracted data.

#### Example Form Processing Code:
```python
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data.get("phone", "N/A"), data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")
```

### 3. Test the Email Functionality
#### Tasks:
- Ensure the `.env` file contains valid `FROM_EMAIL`, `PASSWORD`, and `TO_EMAIL` values.
- Test sending an email using the `send_email` function with:
  - Correct SMTP server configurations.
  - Proper error handling for invalid credentials or network issues.

### 4. Update `index.html` and `base.html` (if applicable)
#### Tasks:
- Add navigation links for the `Contact` page in the base layout (`base.html`) or homepage (`index.html`).
- Example:
```html
<nav>
  <a href="/">Home</a>
  <a href="/about">About</a>
  <a href="/contact">Contact</a>
</nav>
```

### 5. Verify Frontend-Backend Integration
#### Tasks:
- Test the full flow:
  - Navigate to `/contact`.
  - Fill out the form and submit it.
  - Verify that a success message appears on the page.
  - Check that the email is received at the `TO_EMAIL` address.

---

## Deliverables
1. Updated `contact.html` with a functional HTML form.
2. Working `send_email` function to handle form submissions and send emails.
3. Fully functional contact page with feedback for successful or failed submissions.
4. Updated `.env` file with correct email credentials (not included in source control).

---

## Notes
- Use CSS to style the form for a polished user experience.
- Add error handling for invalid input or email failures.
- Ensure sensitive data (e.g., email credentials) is never exposed in the codebase.

