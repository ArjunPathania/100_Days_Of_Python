# Task: Update HTML Forms to Use Flask-WTF Forms

## Objective
Enhance the Flask application by integrating Flask-WTF forms into the HTML templates. This will improve form handling, validation, and maintainability.

---

## Steps

### 1. Update `login.html` Template
#### Tasks:
- Replace the current static HTML form with Flask-WTF's `form` object.
- Use Bootstrap classes for styling and ensure compatibility with Flask-Bootstrap5.

#### Example Updated `login.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    {{ bootstrap.load_css() }}
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center">Login</h1>
        <form method="POST">
            {{ form.hidden_tag() }}

            <div class="mb-3">
                {{ form.email.label(class="form-label") }}
                {{ form.email(class="form-control") }}
                {% if form.email.errors %}
                    <div class="text-danger">
                        {{ form.email.errors[0] }}
                    </div>
                {% endif %}
            </div>

            <div class="mb-3">
                {{ form.password.label(class="form-label") }}
                {{ form.password(class="form-control") }}
                {% if form.password.errors %}
                    <div class="text-danger">
                        {{ form.password.errors[0] }}
                    </div>
                {% endif %}
            </div>

            <div class="text-center">
                {{ form.submit(class="btn btn-primary") }}
            </div>
        </form>
    </div>
    {{ bootstrap.load_js() }}
</body>
</html>
```

### 2. Add Templates for Success and Denied Pages
#### Tasks:
- Create `success.html` and `denied.html` templates to display login outcomes.

#### Example `success.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Success</title>
</head>
<body>
    <h1>Welcome! Login Successful.</h1>
</body>
</html>
```

#### Example `denied.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Denied</title>
</head>
<body>
    <h1>Access Denied. Please check your credentials.</h1>
</body>
</html>
```

### 3. Configure Bootstrap Integration
#### Tasks:
- Ensure `base.html` or individual templates include Bootstrap CSS and JS using `{{ bootstrap.load_css() }}` and `{{ bootstrap.load_js() }}`.
- Optionally, create a `base.html` template for a consistent layout.

#### Example `base.html`:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Flask App{% endblock %}</title>
    {{ bootstrap.load_css() }}
</head>
<body>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    {{ bootstrap.load_js() }}
</body>
</html>
```
- Update `login.html`, `success.html`, and `denied.html` to extend this base template.

### 4. Test the Application
#### Tasks:
- Run the application locally (`python app.py`).
- Navigate to `/login` and verify:
  - Form displays correctly with Bootstrap styling.
  - Validation messages appear for invalid input.
  - Successful login redirects to the success page.
  - Failed login redirects to the denied page.

---

## Deliverables
1. Updated `login.html` using Flask-WTF and Bootstrap.
2. New `success.html` and `denied.html` templates.
3. (Optional) Base template (`base.html`) for consistent styling.
4. Fully functional login page with proper form handling and validation.

---

## Notes
- Ensure `app.secret_key` is set to a secure value.
- Add tests for edge cases (e.g., invalid email format, short passwords).
- Consider integrating Flask-Flash for user feedback on failed login attempts.

