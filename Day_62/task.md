# Day 62 - 100DaysOfPython Challenge

## Project Title: Coffee & Wi-Fi Web App

---

### Objective:
Create a Flask-based web application using WTForms, Bootstrap-Flask, and CSV for managing cafe information. The app should include the following functionality:

1. Render a visually appealing home page styled with CSS and Bootstrap.
2. Display a list of cafes with their details in a Bootstrap table.
3. Provide a hidden route to add new cafes via a form.
4. Validate form inputs and dynamically update the cafe list by appending new data to the CSV file.

---

### Requirements:

#### 1. Home Page:
- Use the `css/styles.css` file for styling.
- Add Bootstrap blocks to `base.html` and link to the stylesheet.
- Include a "Show Me!" button that navigates to the `/cafes` route.

#### 2. Cafes Page:
- Render the `cafes.html` file.
- Display cafe data from `cafe-data.csv` in a Bootstrap table.
- Replace location URLs with anchor tags labeled "Maps Link" that redirect to the actual location.
  - **Hint:** All location links start with "http".

#### 3. Secret Add Page:
- Create a hidden route `/add` that renders the `add.html` file.
- Use WTForms and `render_form` to create a form for entering new cafe details.
- Include the following form fields:
  - Cafe Name
  - Location URL (validated to ensure proper format)
  - Open Time
  - Close Time
  - Coffee Rating
  - Wi-Fi Strength Rating
  - Power Outlet Availability

#### 4. CSV Data Handling:
- Upon successful form submission:
  - Append new data to `cafe-data.csv` as a comma-separated line.
  - Ensure all fields are included and properly formatted.

#### 5. Navigation:
- Ensure all navigation links in the app work seamlessly.

---

### Hints & Resources:

1. **WTForms Documentation:** [Quickstart Guide](https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/)
2. **Bootstrap-Flask:** [Macros Documentation](https://bootstrap-flask.readthedocs.io/en/stable/macros/#render-form)
3. **WTForms Validators:** [URL Validation](https://wtforms.readthedocs.io/en/2.3.x/validators/)
4. **Turn Off Client-Side Validation:** [StackOverflow Solution](https://stackoverflow.com/a/61166621/10557313)
5. **File Write in Python:** [W3Schools Guide](https://www.w3schools.com/python/python_file_write.asp)

---

### Submission Checklist:
- [ ] Home page matches the desired design and links correctly.
- [ ] Cafes page displays all CSV data in a styled Bootstrap table.
- [ ] Location URLs are formatted as clickable anchor tags.
- [ ] Add page form works with proper validation.
- [ ] New cafe data is successfully appended to `cafe-data.csv`.
- [ ] Navigation links are functional across all pages.
