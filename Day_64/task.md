# Task: Build a "Top Movies" Web Application with SQLAlchemy

## Objective
Create a web application that allows users to manage their top movies. Users can add, edit, and delete movies, as well as assign ratings to them. The app uses SQLAlchemy for database interactions and Flask for the web interface.

---

## Steps

### 1. Set Up the Database
#### Tasks:
- Create an SQLite database named `movies.db`.
- Define a `Movie` model with the following attributes:
  - `id` (Integer, primary key)
  - `title` (String, unique, required)
  - `director` (String, required)
  - `rating` (Float, required)

#### Example Code:
```python
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    director: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()
```

### 2. Implement the Home Page
#### Tasks:
- Create a route for `/` to display all movies in the database.
- Query the database for all movies and pass them to the `index.html` template.

#### Example Code:
```python
@app.route('/')
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.title))
    all_movies = result.scalars().all()
    return render_template("index.html", movies=all_movies)
```

#### Example HTML (`index.html`):
- Display movies in a table with options to edit or delete each movie.
```html
<table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Director</th>
            <th>Rating</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for movie in movies %}
        <tr>
            <td>{{ movie.title }}</td>
            <td>{{ movie.director }}</td>
            <td>{{ movie.rating }}</td>
            <td>
                <a href="/edit?id={{ movie.id }}">Edit</a>
                <a href="/delete?movie_id={{ movie.id }}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

### 3. Add New Movies
#### Tasks:
- Create a route for `/add` to handle adding new movies.
- Use a `POST` request to submit a form with the movie's title, director, and rating.

#### Example Code:
```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_movie = Movie(
            title=request.form["title"],
            director=request.form["director"],
            rating=request.form["rating"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')
```

#### Example HTML (`add.html`):
```html
<form method="POST">
    <label for="title">Title:</label>
    <input type="text" id="title" name="title" required>

    <label for="director">Director:</label>
    <input type="text" id="director" name="director" required>

    <label for="rating">Rating:</label>
    <input type="number" id="rating" name="rating" step="0.1" required>

    <button type="submit">Add Movie</button>
</form>
```

### 4. Edit Movie Ratings
#### Tasks:
- Create a route for `/edit` to handle editing movie ratings.
- Use a form to update the rating of a selected movie.

#### Example Code:
```python
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        movie_id = request.form["id"]
        movie_to_update = db.get_or_404(Movie, movie_id)
        movie_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    return render_template("edit.html", movie=movie_selected)
```

#### Example HTML (`edit.html`):
```html
<form method="POST">
    <input type="hidden" name="id" value="{{ movie.id }}">

    <label for="rating">Rating:</label>
    <input type="number" id="rating" name="rating" value="{{ movie.rating }}" step="0.1" required>

    <button type="submit">Update Rating</button>
</form>
```

### 5. Delete Movies
#### Tasks:
- Create a route for `/delete` to handle deleting movies by ID.
- Redirect to the home page after deletion.

#### Example Code:
```python
@app.route("/delete")
def delete():
    movie_id = request.args.get('movie_id')
    if not movie_id:
        return "Movie ID is required", 400
    movie_to_delete = db.get_or_404(Movie, movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
```

---

## Deliverables
1. A fully functional web app with:
   - Home page displaying all movies.
   - Add, edit, and delete functionalities.
2. HTML templates (`index.html`, `add.html`, `edit.html`).
3. SQLite database to store movies.
4. SQLAlchemy models and Flask routes for all CRUD operations.

---

## Notes
- Ensure the app runs without errors (`python app.py`).
- Use Bootstrap or another CSS framework for styling if desired.
- Test all features thoroughly to ensure data integrity and proper navigation.

