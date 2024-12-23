# Blog Website Task

This document outlines the tasks required to create a blog website using Flask. The website includes the following functionalities:

- Displaying all blog posts on the homepage.
- Providing an "About" page.
- Providing a "Contact" page.
- Displaying individual blog posts with unique URLs.

## Task Breakdown

### 1. Project Setup
- **Install Flask**:
  Ensure Flask is installed in your environment.
  ```bash
  pip install flask
  ```

- **Directory Structure**:
  Set up the directory structure as follows:
  ```
  project_directory/
  |-- templates/
  |   |-- index.html
  |   |-- about.html
  |   |-- contact.html
  |   |-- post.html
  |-- app.py
  ```

### 2. Backend Development
- **Fetch Blog Posts**:
  Use the `requests` library to fetch blog data from the provided API endpoint (`https://api.npoint.io/447af222d6804d293c72`).
  
  Example:
  ```python
  import requests

  posts = requests.get(url='https://api.npoint.io/447af222d6804d293c72').json()
  ```

- **Flask Routes**:
  Implement the following routes:
  
  | Route         | Functionality                             |
  |---------------|------------------------------------------|
  | `/`           | Displays all blog posts.                 |
  | `/about`      | Renders the "About" page.                |
  | `/contact`    | Renders the "Contact" page.              |
  | `/post/<int>` | Displays a single blog post by its ID.   |

  Example:

[//]: # (  ```python)

[//]: # (  @app.route&#40;'/'&#41;)

[//]: # (  def get_all_posts&#40;&#41;:)

[//]: # (      return render_template&#40;'index.html', all_posts=posts&#41;)

[//]: # ()
[//]: # (  @app.route&#40;'/about'&#41;)

[//]: # (  def about&#40;&#41;:)

[//]: # (      return render_template&#40;'about.html'&#41;)

[//]: # ()
[//]: # (  @app.route&#40;'/contact'&#41;)

[//]: # (  def contact&#40;&#41;:)

[//]: # (      return render_template&#40;'contact.html'&#41;)

[//]: # ()
[//]: # (  @app.route&#40;'/post/<int:index>'&#41;)

[//]: # (  def show_post&#40;index&#41;:)

[//]: # (      requested_post = next&#40;&#40;post for post in posts if post["id"] == index&#41;, None&#41;)

[//]: # (      return render_template&#40;'post.html', post=requested_post&#41;)

[//]: # (  ```)

- **Run the Server**:
  Use `app.run(debug=True)` to run the development server.

### 3. Frontend Development
- **Create Templates**:
  Design and create the following templates:

  - **`index.html`**:
    Display a list of all blog posts with links to individual posts.
  
  - **`about.html`**:
    Provide information about the blog or website owner.
  
  - **`contact.html`**:
    Include a contact form or details for reaching out.
  
  - **`post.html`**:
    Display the content of a single blog post.

  Example HTML Structure:
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <title>Blog</title>
  </head>
  <body>
      <h1>Welcome to the Blog</h1>
      {% for post in all_posts %}
      <h2><a href="/post/{{ post.id }}">{{ post.title }}</a></h2>
      <p>{{ post.subtitle }}</p>
      {% endfor %}
  </body>
  </html>
  ```

### 4. Testing
- Test the application locally by running `app.py`.
- Verify:
  - All posts appear on the homepage.
  - Individual posts render correctly.
  - The "About" and "Contact" pages load as expected.

### 5. Deployment (Optional)
- Deploy the Flask app to a hosting service such as Heroku, PythonAnywhere, or AWS.
- Ensure that the API endpoint for fetching posts is accessible.

## Additional Notes
- Use CSS to style the templates for a better user experience.
- Handle potential errors (e.g., invalid post IDs or API request failures).
- Optimize the layout for mobile and desktop views.

